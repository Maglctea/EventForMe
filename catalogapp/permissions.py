from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser


class VendorReadonlyPermission(BasePermission):
    """
        Пользовательский класс разрешений для группы поставщиков,
        который разрешает доступ только для чтения к объектам Bride.
    """

    def has_permission(self, request, view):
        # Проверяем, принадлежит ли пользователь к группе "vendor"
        if request.user.groups.filter(name='vendor').exists():
            # Проверяем, безопасен ли метод запроса (GET, HEAD, or OPTIONS)
            if request.method in ['GET', 'HEAD', 'OPTIONS']:
                return True

        return False


class VendorPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='bride').exists():
            return False
        elif request.user.groups.filter(name='vendor').exists():
            # Vendor  users может выполнять POST, PUT, and DELETE запросы
            return True
        # По умолчанию запрещается разрешение, если пользователь не принадлежит ни к одной группе
        return False


class BrideReadonlyPermission(BasePermission):
    """
           Пользовательский класс разрешений для группы bride,
           который разрешает доступ только для чтения к объектам Vendor.
    """

    def has_permission(self, request, view):
        # Проверяем, принадлежит ли пользователь к группе "bride"
        if request.user.groups.filter(name='bride').exists():
            # Проверяем, безопасен ли метод запроса (GET, HEAD, or OPTIONS)
            if request.method in ['GET', 'HEAD', 'OPTIONS']:
                return True
        return False


class BridePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='vendor').exists():
            return False
        elif request.user.groups.filter(name='bride').exists():
            # Bride  users может выполнять POST, PUT, and DELETE запросы
            return True
        # По умолчанию запрещается разрешение, если пользователь не принадлежит ни к одной группе
        return False


class VendorCanCreatePermission(BasePermission):
    def has_permission(self, request, view):
        request.method == 'POST' and request.user.groups.filter(name='vendor').exists()


class AdminCanCreatePermission(BasePermission):
    def has_permission(self, request, view):
        request.method == 'POST' and IsAdminUser().has_permission(request, view)


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
