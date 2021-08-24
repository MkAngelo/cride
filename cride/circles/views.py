"""Circle views."""

# Django
from django.http import HttpResponse


def list_circles(request):
    """List circles"""
    return HttpResponse('Hola')