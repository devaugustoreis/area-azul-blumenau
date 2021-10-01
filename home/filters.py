from django.db.models import fields
import django_filters
from .models import *

class VehicleFilter(django_filters.FilterSet):
    class Meta:
        model = Vehicle
        fields = '__all__'