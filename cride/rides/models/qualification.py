"""Ride Qualification."""

# Django
from cride.circles.models.circles import Circle
from django.db import models

# Utilities
from cride.utils.models import CRideModel


class Qualification(CRideModel):
    """Qualification model."""

    circle = models.ForeignKey('crides.Cride', on_delete=models.DO_NOTHING)
    proflie = models.ForeignKey('users.Profile', on_delete=models.DO_NOTHING)
    ride = models.ForeignKey('rides.Ride', on_delete=models.DO_NOTHING)
    passenger = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)

    reputation = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        """Return username and reputation."""
        return f'{self.user.username} give you {self.user.reputation} stars.'