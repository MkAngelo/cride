"""Invitation model."""

# Django 
from django.db import models
from django.db.models.fields import CharField

# Utilities
from cride.utils.models import CRideModel

# Managers
from cride.circles.managers.invitations import InvitationManager


class Invitation(CRideModel):
    """Invitation model.
    
    A member can invite someone joins to a Circle, if the member is admin.
    """

    code = CharField(max_length=50, unique=True)
    circle = models.ForeignKey('circles.Circle', on_delete=models.CASCADE)
    issued_by = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        help_text='Member of the circle that issue invitation',
        related_name='issued_by'
    )
    used_by = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=True,
        help_text='User that uses the invitation.'
    )
    used = models.BooleanField(default=False)
    used_at = models.DateTimeField(blank=True, null=True)

    # Manager
    objects = InvitationManager()

    def __str__(self):
        """Return code and circle."""
        return f'#{self.circle.slug_name}: {self.code}'