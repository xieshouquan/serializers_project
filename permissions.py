from rest_framework.permissions import BasePermission
from serializer_lesson.models import User

class ProductPermissionAny(BasePermission):
    def has_permission(self, request, view):
        from serializer_lesson.views import ProductCategoryView,ProductView
        if isinstance(view,(ProductView,ProductCategoryView)):
            return True

        return False

    # def has_object_permission(self, request, view, obj):
    #     if isinstance(obj,User):
    #         return False
    #     return True