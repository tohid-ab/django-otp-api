# from rest_framework.permissions import BasePermission, SAFE_METHODS
#
#
# class IsAuthenticated(BasePermission):
#     def has_permission(self, request, view):
#         return bool(request.user)
#
#
# class IsSuperUser(BasePermission):
#     def has_permission(self, request, view):
#         return bool(request.user.is_superuser)
#
#
# class IsUser(BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         if request.user:
#             if request.user.is_superuser:
#                 return True
#             else:
#                 return obj.author.id == request.user.id
#         else:
#             return False