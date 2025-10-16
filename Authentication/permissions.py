from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    فقط کاربرانی با نقش 'admin' اجازه دارند
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.role and request.user.role.name == "admin"
        )


class IsAuthor(BasePermission):
    """
    فقط کاربرانی با نقش 'author' اجازه دارند
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.role and request.user.role.name == "author"
        )


class IsMember(BasePermission):
    """
    فقط کاربرانی با نقش 'member' اجازه دارند
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.role and request.user.role.name == "member"
        )


class IsAdminOrAuthor(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.role
            and request.user.role.name in ["admin", "author"]
        )