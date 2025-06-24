# In order to create custom permission class we need import permission model from Django framewoek
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission): # This is the basepermission class that Django framework provide for making custom permission.
    """Allow user to edit thier own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit thier own profile"""

        if request.method is permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
