from django.db.models import fields
import django_filters
from django_filters.filters import ModelChoiceFilter, ModelMultipleChoiceFilter, NumberFilter
from .models import *
from django_filters import DateFilter

# class VehicleFilter(django_filters.FilterSet):
#     class Meta:
#         model = Vehicle
#         fields = '__all__'


class OperationsFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr="gte")
    end_date = DateFilter(field_name="date", lookup_expr="lte")
    # vehicle = filters.ModelChoiceFilter(queryset=departments)
    start_value = NumberFilter(field_name="value", lookup_expr="gte")
    end_value = NumberFilter(field_name="value", lookup_expr="lte")
    class Meta:
        model = Operation
        fields = ['operation_type', 'payment_method', 'vehicle']