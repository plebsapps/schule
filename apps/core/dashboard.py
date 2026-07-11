from django.db.models import Count, Q

from apps.accounts.models import User
from apps.classes.models import SchoolClass
from apps.grades.models import GradeSheet
from apps.schools.models import ReportPeriod


def build_dashboard(user):
    can_view_all = user.is_superuser or user.role in {User.Role.ADMIN, User.Role.SCHOOL_MANAGEMENT}
    classes = SchoolClass.objects.filter(is_active=True)
    if not can_view_all:
        classes = classes.filter(Q(class_teacher=user) | Q(teaching_assignments__teacher=user))

    classes = (
        classes.select_related("school_year", "school_year__school", "class_teacher")
        .annotate(
            student_count=Count("enrollments__student", distinct=True),
            subject_count=Count("teaching_assignments__subject", distinct=True),
            completed_count=Count(
                "teaching_assignments__grade_sheet",
                filter=Q(teaching_assignments__grade_sheet__status=GradeSheet.Status.COMPLETED),
                distinct=True,
            ),
        )
        .distinct()
        .order_by("school_year__start_date", "name")
    )
    class_rows = list(classes)
    class_ids = [school_class.pk for school_class in class_rows]
    school_year_ids = {school_class.school_year_id for school_class in class_rows}

    open_periods = ReportPeriod.objects.filter(
        school_year_id__in=school_year_ids,
        status=ReportPeriod.Status.OPEN,
    )
    current_period = (
        open_periods.select_related("school_year").order_by("-school_year__start_date", "start_date").first()
    )

    student_count = (
        SchoolClass.objects.filter(pk__in=class_ids).aggregate(value=Count("enrollments__student", distinct=True))[
            "value"
        ]
        or 0
    )
    subject_count = (
        SchoolClass.objects.filter(pk__in=class_ids).aggregate(
            value=Count("teaching_assignments__subject", distinct=True)
        )["value"]
        or 0
    )

    class_data = []
    tasks = []
    for school_class in class_rows:
        lead = school_class.class_teacher
        class_data.append(
            {
                "name": school_class.name,
                "school": school_class.school_year.school.name,
                "school_year": school_class.school_year.name,
                "lead": lead.get_full_name() or lead.username if lead else "Nicht zugewiesen",
                "students": school_class.student_count,
                "subjects": school_class.subject_count,
                "status": f"{school_class.completed_count}/{school_class.subject_count} Fächer abgeschlossen"
                if school_class.student_count and school_class.subject_count
                else "Einrichtung offen",
            }
        )
        if school_class.student_count == 0:
            tasks.append(
                {
                    "title": "Schüler zuordnen",
                    "context": f"Klasse {school_class.name} enthält noch keine Schüler.",
                    "priority": "Stammdaten",
                }
            )
        if school_class.subject_count == 0:
            tasks.append(
                {
                    "title": "Unterricht zuordnen",
                    "context": f"Klasse {school_class.name} besitzt noch keine Fachzuordnung.",
                    "priority": "Stammdaten",
                }
            )

    if not class_data:
        tasks.append(
            {
                "title": "Keine zugewiesenen Klassen",
                "context": "Eine berechtigte Verwaltung kann Klassen- oder Unterrichtszuordnungen anlegen.",
                "priority": "Hinweis",
            }
        )
    elif not tasks:
        tasks.append(
            {
                "title": "Stammdaten vollständig verbunden",
                "context": "Der nächste Entwicklungsschritt ist die geschützte Noteneingabe.",
                "priority": "Nächste Phase",
            }
        )

    school_year_names = sorted({school_class.school_year.name for school_class in class_rows}, reverse=True)
    return {
        "school_year": ", ".join(school_year_names) if school_year_names else "Noch kein Schuljahr zugeordnet",
        "period": current_period.name if current_period else "Keine offene Zeugnisperiode",
        "period_is_open": current_period is not None,
        "scope": "Gesamtübersicht" if can_view_all else "Meine Zuordnungen",
        "summary": (
            {"label": "Klassen", "value": len(class_data), "detail": "für Sie sichtbar", "tone": "blue"},
            {"label": "Schüler", "value": student_count, "detail": "in sichtbaren Klassen", "tone": "violet"},
            {"label": "Fächer", "value": subject_count, "detail": "zugewiesene Fächer", "tone": "amber"},
            {
                "label": "Offene Perioden",
                "value": open_periods.count(),
                "detail": "für sichtbare Schuljahre",
                "tone": "green",
            },
        ),
        "classes": class_data,
        "tasks": tasks[:6],
    }
