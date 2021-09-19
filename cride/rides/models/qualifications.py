"""Ride Qualification."""

# Django
from cride.circles.models.circles import Circle
from django.db import models

# Utilities
from cride.utils.models import CRideModel


class Qualification(CRideModel):
    """Qualification model."""
    ride = models.ForeignKey('rides.Ride', on_delete=models.CASCADE, related_name='ride_qualification')
    circle = models.ForeignKey('circles.Circle', on_delete=models.CASCADE)

    reputation_user = models.ForeignKey(
        'users.User',
        on_delete=models.DO_NOTHING,
        null=True,
        help_text="Reputation's user.",
        related_name='reputation_user'
    )

    rated_user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        help_text='User that receives the rating.',
        related_name='rated_user'
    )

    comments = models.TextField(blank=True)
    reputation = models.IntegerField(default=5)

    def __str__(self):
        """Return username and reputation."""
        return f'@{self.reputation_user} rated {self.reputation} stars by @{self.rated_user.username}.'