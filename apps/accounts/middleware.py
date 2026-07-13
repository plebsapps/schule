from django.core.exceptions import PermissionDenied

PASSWORD_CHANGE_VIEW_NAMES = frozenset(
    {
        "admin:password_change",
        "admin:auth_user_password_change",
    }
)


class ReadOnlyAccountMiddleware:
    """Prevent managed read-only accounts from changing passwords themselves."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        user = request.user
        view_name = request.resolver_match.view_name if request.resolver_match else None
        if (
            user.is_authenticated
            and not user.can_change_own_password
            and view_name in PASSWORD_CHANGE_VIEW_NAMES
        ):
            raise PermissionDenied("Das Passwort dieses verwalteten Lesekontos kann nur administrativ geändert werden.")
        return None
