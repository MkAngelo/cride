"""Circles Permissions Classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from cride.circles.models import Membership 


class IsActiveCircleMember(BasePermission):
    """Allow access only to circle memebers.
    
    Expect that views implementing this permissions have a 'circle'
    attribute assigned.
    """

    def has_permission(self, request, view):
        """Verify user is an active member of the circle."""

        try:
            Membership.objects.get(
                user=request.user,
                circle=view.circle,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True


class IsSelfMember(BasePermission):
    """Allow access only if you are the owner of the invitations.

    Expect that "invitation view" implements this permission to restrict only to owner of the invitations.    
    """
    def has_permission(self, request, view):
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self, request, view, obj):
        """Verify if the user is owner."""

        return request.user == obj.user