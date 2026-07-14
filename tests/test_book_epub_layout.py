import re
import subprocess
from pathlib import Path

EPUB_CSS = Path(__file__).resolve().parents[1] / "buch" / "epub.css"
REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def test_book_does_not_name_unrelated_project_subdomains():
    allowed_hosts = {"schule.plebsapps.de"}
    referenced_hosts = set()

    for manuscript_file in (REPOSITORY_ROOT / "buch").glob("*.md"):
        manuscript = manuscript_file.read_text(encoding="utf-8")
        referenced_hosts.update(re.findall(r"(?<![\w.-])([a-z0-9-]+\.plebsapps\.de)", manuscript, re.IGNORECASE))

    assert referenced_hosts <= allowed_hosts


def test_epub_images_are_centered_and_limited_to_page_width():
    css = EPUB_CSS.read_text(encoding="utf-8")

    figure_rule = css.split("figure,", maxsplit=1)[1].split("}", maxsplit=1)[0]
    image_rule = css.split("img,", maxsplit=1)[1].split("}", maxsplit=1)[0]

    assert "#cover-image" in figure_rule
    assert "max-width: 100%;" in figure_rule
    assert "margin-right: auto;" in figure_rule
    assert "margin-left: auto;" in figure_rule
    assert "text-align: center;" in figure_rule
    assert "#cover-image svg" in image_rule
    assert "display: block;" in image_rule
    assert "width: auto;" in image_rule
    assert "max-width: 100%;" in image_rule
    assert "height: auto;" in image_rule
    assert "margin-right: auto;" in image_rule
    assert "margin-left: auto;" in image_rule


def test_epub_code_wraps_within_the_available_page_width():
    css = EPUB_CSS.read_text(encoding="utf-8")

    inline_code_rule = css.split("code {", maxsplit=1)[1].split("}", maxsplit=1)[0]
    pre_rule = css.split("pre {", maxsplit=1)[1].split("}", maxsplit=1)[0]
    pre_code_rule = css.split("pre code {", maxsplit=1)[1].split("}", maxsplit=1)[0]
    highlighted_code_rule = css.split("pre code span,", maxsplit=1)[1].split("}", maxsplit=1)[0]
    table_code_rule = css.split("th code,", maxsplit=1)[1].split("}", maxsplit=1)[0]

    assert "overflow-wrap: anywhere;" in inline_code_rule
    assert "word-break: break-word;" in inline_code_rule
    assert "box-sizing: border-box;" in pre_rule
    assert "min-width: 0;" in pre_rule
    assert "max-width: 100%;" in pre_rule
    assert "overflow-wrap: anywhere;" in pre_rule
    assert "word-break: break-word;" in pre_rule
    assert "white-space: pre-wrap;" in pre_rule
    assert "break-inside: auto;" in pre_rule
    assert "page-break-inside: auto;" in pre_rule
    assert "box-decoration-break: clone;" in pre_rule
    assert "display: block;" in pre_code_rule
    assert "max-width: 100%;" in pre_code_rule
    assert "overflow-wrap: inherit;" in pre_code_rule
    assert "word-break: break-all;" in pre_code_rule
    assert "white-space: pre-wrap !important;" in pre_code_rule
    assert "pre code a" in highlighted_code_rule
    assert "overflow-wrap: anywhere;" in highlighted_code_rule
    assert "word-break: break-all;" in highlighted_code_rule
    assert "td code" in table_code_rule
    assert "white-space: normal;" in table_code_rule
    assert "overflow-wrap: anywhere;" in table_code_rule


def test_epub_tables_fit_the_page_and_remain_readable():
    css = EPUB_CSS.read_text(encoding="utf-8")

    table_rule = css.split("table {", maxsplit=1)[1].split("}", maxsplit=1)[0]
    cell_rule = css.split("\nth,\ntd {", maxsplit=1)[1].split("}", maxsplit=1)[0]

    assert "box-sizing: border-box;" in table_rule
    assert "width: 100%;" in table_rule
    assert "max-width: 100%;" in table_rule
    assert "table-layout: fixed;" in table_rule
    assert "font-size: 0.74em;" in table_rule
    assert "overflow-wrap: anywhere;" in table_rule
    assert "word-break: break-word;" in table_rule
    assert "min-width: 0;" in cell_rule
    assert "hyphens: auto;" in cell_rule
    assert "overflow-wrap: anywhere;" in cell_rule


def test_epub_uses_a_consistent_print_layout():
    css = EPUB_CSS.read_text(encoding="utf-8")

    body_rule = css.split("body {", maxsplit=1)[1].split("}", maxsplit=1)[0]
    headings_rule = css.split("h1,", maxsplit=1)[1].split("}", maxsplit=1)[0]
    figure_rule = css.split("figure,", maxsplit=1)[1].split("}", maxsplit=1)[0]
    caption_rule = css.split("figcaption {", maxsplit=1)[1].split("}", maxsplit=1)[0]
    pre_rule = css.split("pre {", maxsplit=1)[1].split("}", maxsplit=1)[0]

    assert "margin: 5%;" in body_rule
    assert "line-height: 1.55;" in body_rule
    assert "hyphens: auto;" in body_rule
    assert "break-after: avoid;" in headings_rule
    assert "page-break-after: avoid;" in headings_rule
    assert "break-inside: avoid;" in figure_rule
    assert "page-break-inside: avoid;" in figure_rule
    assert "font-size: 0.82em;" in caption_rule
    assert "text-align: center;" in caption_rule
    assert "break-inside: auto;" in pre_rule
    assert "page-break-inside: auto;" in pre_rule


def test_early_git_code_block_can_split_safely_in_paginated_readers():
    chapter = (REPOSITORY_ROOT / "buch" / "01-projektstart-planung-repository.md").read_text(encoding="utf-8")
    css = EPUB_CSS.read_text(encoding="utf-8")

    assert "git remote add origin" in chapter
    assert "page-break-inside: auto;" in css
    assert "white-space: pre-wrap !important;" in css
    assert "word-break: break-all;" in css


def test_book_documents_project_access_repository_and_privacy_boundary():
    book_readme = (REPOSITORY_ROOT / "buch" / "README.md").read_text(encoding="utf-8")
    final_chapter = (REPOSITORY_ROOT / "buch" / "10-showcase-abschluss-lesekonto-systemd.md").read_text(
        encoding="utf-8"
    )
    combined = book_readme + final_chapter

    assert "https://schule.plebsapps.de" in combined
    assert "https://github.com/plebsapps/schule" in combined
    assert "`Buch`" in combined
    assert "VPN" in combined
    assert "GPLv3" in combined
    assert "Issues" in combined
    assert "Pull Requests" in combined
    assert "Releases" in combined
    assert "Echte Schülerdaten" in combined
    assert "öffentlich über das Internet" in combined
    assert "Schulnetz" in combined


def test_chapter_ten_starts_with_public_read_only_demo_access_box():
    chapter = (REPOSITORY_ROOT / "buch" / "10-showcase-abschluss-lesekonto-systemd.md").read_text(encoding="utf-8")
    css = EPUB_CSS.read_text(encoding="utf-8")
    lines = chapter.splitlines()

    assert lines[0] == "# Kapitel 10: Show-case-Abschluss, Systemstart und Lesekonto"
    assert lines[2] == "::: {.demo-access}"
    assert "**URL:** [https://schule.plebsapps.de](https://schule.plebsapps.de)" in chapter
    assert "**Benutzer:** `Buch`" in chapter
    assert "**Passwort:** `BuchPW$1`" in chapter
    assert "ausschließlich Leserechte" in chapter
    assert "das eigene Passwort nicht ändern" in chapter

    demo_access_rule = css.split(".demo-access {", maxsplit=1)[1].split("}", maxsplit=1)[0]
    assert "box-sizing: border-box;" in demo_access_rule
    assert "max-width: 100%;" in demo_access_rule
    assert "overflow-wrap: anywhere;" in demo_access_rule
    assert "break-inside: avoid;" in demo_access_rule
    assert "page-break-inside: avoid;" in demo_access_rule


def test_book_does_not_contain_its_own_download_url():
    download_path = "/arbeiten-mit-openai-codex.epub"

    for manuscript_file in (REPOSITORY_ROOT / "buch").glob("*.md"):
        manuscript = manuscript_file.read_text(encoding="utf-8")
        assert download_path not in manuscript, f"Download-Link in {manuscript_file.name} gefunden"


def test_book_consistently_describes_itself_as_a_practical_example():
    book_sources = list((REPOSITORY_ROOT / "buch").glob("*.md"))
    book_sources.append(REPOSITORY_ROOT / "buch" / "metadata.yaml")

    for book_source in book_sources:
        content = book_source.read_text(encoding="utf-8").lower()
        assert "lehrbuch" not in content, f"Abweichende Buchbezeichnung in {book_source.name} gefunden"

    book_readme = (REPOSITORY_ROOT / "buch" / "README.md").read_text(encoding="utf-8")
    assert "Ziel dieses Praxisbeispiels" in book_readme


def test_prompt_headings_use_short_labels_after_single_editorial_notice():
    foreword = (REPOSITORY_ROOT / "buch" / "Vorwort.md").read_text(encoding="utf-8")
    normalized_foreword = " ".join(foreword.split())
    markdown_files = list((REPOSITORY_ROOT / "buch").glob("*.md"))
    headings = [
        line
        for markdown_file in markdown_files
        for line in markdown_file.read_text(encoding="utf-8").splitlines()
        if line.startswith("#")
    ]

    assert "Ein einmaliger redaktioneller Hinweis gilt für das gesamte Buch" in foreword
    assert "keine wörtlichen Transkripte" in normalized_foreword
    assert not any("Redaktionell überarbeitet" in heading for heading in headings)
    assert any(heading.endswith(" Prompt") for heading in headings)
    assert any(heading.endswith(" Arbeitsauftrag") for heading in headings)


def test_markdown_tables_have_consistent_rows_and_at_most_six_columns():
    for markdown_file in (REPOSITORY_ROOT / "buch").glob("*.md"):
        table_column_count = None

        for line in markdown_file.read_text(encoding="utf-8").splitlines():
            if not line.startswith("|"):
                table_column_count = None
                continue

            column_count = line.count("|") - 1
            if table_column_count is None:
                table_column_count = column_count

            assert 2 <= column_count <= 6, f"Überbreite Tabelle in {markdown_file.name}: {line}"
            assert column_count == table_column_count, f"Inkonsistente Tabellenzeile in {markdown_file.name}: {line}"


def test_book_manuscripts_use_a_consistent_heading_hierarchy():
    manuscript_files = sorted((REPOSITORY_ROOT / "buch").glob("[0-9][0-9]-*.md"))
    manuscript_files.extend(
        [
            REPOSITORY_ROOT / "buch" / "bildkonzept.md",
            REPOSITORY_ROOT / "buch" / "Author.md",
            REPOSITORY_ROOT / "buch" / "anhang-codex-kommandoreferenz.md",
            REPOSITORY_ROOT / "buch" / "glossar.md",
            REPOSITORY_ROOT / "buch" / "quellenverzeichnis.md",
            REPOSITORY_ROOT / "buch" / "projektchronik.md",
        ]
    )

    for manuscript_file in manuscript_files:
        heading_levels = [
            len(line) - len(line.lstrip("#"))
            for line in manuscript_file.read_text(encoding="utf-8").splitlines()
            if line.startswith("#") and line.lstrip("#").startswith(" ")
        ]

        assert heading_levels[0] == 1, f"Erste Überschrift ist nicht H1: {manuscript_file.name}"
        assert heading_levels.count(1) == 1, f"Mehr als eine H1-Überschrift: {manuscript_file.name}"
        assert max(heading_levels) <= 3, f"Zu tiefe Überschriftenebene: {manuscript_file.name}"
        assert all(
            current <= previous + 1 for previous, current in zip(heading_levels, heading_levels[1:], strict=False)
        ), f"Überschriftenebene übersprungen: {manuscript_file.name}"


def test_book_build_contains_all_numbered_chapters_in_order():
    chapter_files = sorted((REPOSITORY_ROOT / "buch").glob("[0-9][0-9]-*.md"))
    build_script = (REPOSITORY_ROOT / "scripts" / "build-book-epub.sh").read_text(encoding="utf-8")

    assert len(chapter_files) == 10

    previous_position = -1
    for number, chapter_file in enumerate(chapter_files, start=1):
        heading = chapter_file.read_text(encoding="utf-8").splitlines()[0]
        script_path = f"buch/{chapter_file.name}"
        position = build_script.index(script_path)

        assert heading.startswith(f"# Kapitel {number}:")
        assert position > previous_position
        previous_position = position


def test_committed_epub_contains_only_well_formed_xml_documents():
    epub = REPOSITORY_ROOT / "static" / "downloads" / "arbeiten-mit-openai-codex.epub"
    validator = REPOSITORY_ROOT / "scripts" / "validate_epub.py"

    result = subprocess.run(
        ["python3", str(validator), str(epub)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr or result.stdout


def test_epub_build_normalizes_raw_html_line_breaks_and_validates_output():
    build_script = (REPOSITORY_ROOT / "scripts" / "build-book-epub.sh").read_text(encoding="utf-8")
    xhtml_filter = (REPOSITORY_ROOT / "buch" / "epub-xhtml.lua").read_text(encoding="utf-8")

    assert "--lua-filter=buch/epub-xhtml.lua" in build_script
    assert 'element.text:match("^<br%s*/?>$")' in xhtml_filter
    assert "pandoc.LineBreak()" in xhtml_filter
    assert 'scripts/validate_epub.py" "$output_file"' in build_script


def test_foreword_explains_prerequisites_and_is_built_before_chapter_one():
    foreword_path = REPOSITORY_ROOT / "buch" / "Vorwort.md"
    foreword = foreword_path.read_text(encoding="utf-8")
    build_script = (REPOSITORY_ROOT / "scripts" / "build-book-epub.sh").read_text(encoding="utf-8")

    assert foreword.startswith("# Vorwort\n")
    assert foreword.count("\n# ") == 0
    assert "## Die wichtigsten Grundlagen in Kürze" in foreword
    assert "## Was dieses Buch nicht vermittelt" in foreword
    assert "## Fehlendes Wissen darf nachgearbeitet werden" in foreword
    assert "Linux" in foreword
    assert "PuTTY" in foreword
    assert "Webserver" in foreword
    assert "Codex" in foreword
    assert "offizielle Dokumentationen" in foreword
    assert "gezielte Internetsuchen" in foreword
    assert "KI-Assistenz" in foreword
    assert "personenbezogene Daten" in foreword
    assert build_script.index("buch/Vorwort.md") < build_script.index("buch/01-projektstart-planung-repository.md")


def test_gpt_5_6_chapter_contains_comparisons_examples_and_official_sources():
    chapter = (REPOSITORY_ROOT / "buch" / "05-was-ist-neu-in-gpt-5-6.md").read_text(encoding="utf-8")

    assert "# Kapitel 5: Was ist neu in GPT-5.6?" in chapter
    assert "## Ausgewählte offizielle Vergleichswerte" in chapter
    assert "## Praxisbeispiele aus diesem Projekt" in chapter
    assert chapter.count("|---") >= 4
    assert "https://openai.com/index/gpt-5-6/" in chapter
    assert "https://help.openai.com/en/articles/20001354" in chapter
    assert "Abrufdatum aller Quellen: **12. Juli 2026**" in chapter


def test_gpt_5_6_model_tiers_chapter_is_a_sourced_decision_guide():
    chapter = (REPOSITORY_ROOT / "buch" / "06-sol-terra-luna-vergleich.md").read_text(encoding="utf-8")

    assert "# Kapitel 6: GPT-5.6 Sol, Terra und Luna im Vergleich" in chapter
    assert "## Vergleich auf einen Blick" in chapter
    assert "## Entscheidungshilfe für die Praxis" in chapter
    assert "## Praxisbeispiele aus der Zeugnisverwaltung" in chapter
    assert "`gpt-5.6-sol`" in chapter
    assert "`gpt-5.6-terra`" in chapter
    assert "`gpt-5.6-luna`" in chapter
    assert chapter.count("|---") >= 2
    assert "https://openai.com/index/gpt-5-6/" in chapter
    assert "https://help.openai.com/en/articles/20001354" in chapter
    assert "Abrufdatum aller Quellen: **12. Juli 2026**" in chapter


def test_sources_directory_contains_public_primary_sources_and_is_built():
    sources = (REPOSITORY_ROOT / "buch" / "quellenverzeichnis.md").read_text(encoding="utf-8")
    build_script = (REPOSITORY_ROOT / "scripts" / "build-book-epub.sh").read_text(encoding="utf-8")

    expected_sources = [
        "https://openai.com/index/gpt-5-6/",
        "https://help.openai.com/en/articles/20001354",
        "https://learn.chatgpt.com/docs/developer-commands?surface=cli",
        "https://learn.chatgpt.com/docs/reference/slash-commands",
        "https://docs.djangoproject.com/en/5.2/releases/5.2/",
        "https://docs.docker.com/compose/",
        "https://www.postgresql.org/docs/current/app-pgdump.html",
        "https://docs.python.org/3.13/",
        "https://pandoc.org/MANUAL.html",
        "https://www.gnu.org/licenses/gpl-3.0.html",
    ]

    assert "Alle Links wurden am **12. Juli 2026**" in sources
    assert all(source in sources for source in expected_sources)
    assert "buch/quellenverzeichnis.md" in build_script


def test_glossary_explains_required_terms_and_is_built():
    glossary = (REPOSITORY_ROOT / "buch" / "glossar.md").read_text(encoding="utf-8")
    build_script = (REPOSITORY_ROOT / "scripts" / "build-book-epub.sh").read_text(encoding="utf-8")

    required_terms = [
        "**Prompt**",
        "**Kontext**",
        "**Skill**",
        "**Plugin**",
        "**MCP**",
        "**Sandbox**",
        "**Migration**",
        "**Pull Request**",
    ]

    assert all(term in glossary for term in required_terms)
    assert "buch/glossar.md" in build_script


def test_book_title_and_subtitle_are_consistent():
    metadata = (REPOSITORY_ROOT / "buch" / "metadata.yaml").read_text(encoding="utf-8")
    book_readme = (REPOSITORY_ROOT / "buch" / "README.md").read_text(encoding="utf-8")
    gallery = (REPOSITORY_ROOT / "templates" / "public" / "image_style_gallery.html").read_text(encoding="utf-8")

    title = "Arbeiten mit OpenAI Codex"
    subtitle = "Praxisbeispiel am Beispiel einer schulischen Zeugnisverwaltung"
    author = "Ralf W. Balz"

    assert f'title: "{title}"' in metadata
    assert f'subtitle: "{subtitle}"' in metadata
    assert f'- "{author}"' in metadata
    assert 'date: "2026-07"' in metadata

    css = EPUB_CSS.read_text(encoding="utf-8")
    assert 'content: "2026 - Juli";' in css
    assert f"# {title}" in book_readme
    assert subtitle in book_readme
    assert title in gallery
    assert subtitle in gallery


def test_author_section_is_consistent_and_included_in_the_book():
    author_section = (REPOSITORY_ROOT / "buch" / "Author.md").read_text(encoding="utf-8")
    build_script = (REPOSITORY_ROOT / "scripts" / "build-book-epub.sh").read_text(encoding="utf-8")

    assert author_section.startswith("# Über den Autor\n")
    assert "Ralf W. Balz" in author_section
    assert "buch/Author.md" in build_script


def test_all_local_book_links_and_images_exist():
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

    for manuscript_file in (REPOSITORY_ROOT / "buch").glob("*.md"):
        for target in link_pattern.findall(manuscript_file.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue

            local_target = target.split("#", maxsplit=1)[0]
            assert (manuscript_file.parent / local_target).resolve().exists(), (
                f"Fehlender lokaler Verweis in {manuscript_file.name}: {target}"
            )
