"""Invitation permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission, IsAdminUser

# Models
from cride.circles.models import Invitation, Membership


class IsSelfMember(BasePermission):
    """Allow access only if you are the owner of the invitations.

    Expect that "invitation view" implements this permission to restrict only to owner of the invitations.    
    """

    def has_object_permission(self, request, view, obj):
        """Verify if the user is owner."""
        
        obj = view.get_object()

        return request.user == obj.user
