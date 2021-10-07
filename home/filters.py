from django.db.models import fields
import django_filters
from .models import *

class VehicleFilter(django_filters.FilterSet):
    class Meta:
        model = Vehicle
        fields = '__all__'


class OperationsFilter(django_filters.FilterSet):
    class Meta:
        model = Operation
        fields = ['date', 'operation_type', 'payment_method', 'vehicle']