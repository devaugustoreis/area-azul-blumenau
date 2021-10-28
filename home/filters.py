from django.db.models import fields
import django_filters
from django_filters.filters import DateFromToRangeFilter, DateRangeFilter, ModelChoiceFilter, ModelMultipleChoiceFilter, NumberFilter
from .models import *
from django_filters import DateFilter


class OperationsFilter(django_filters.FilterSet):
    date_range = DateFromToRangeFilter(field_name='date') 
    start_value = NumberFilter(field_name="value", lookup_expr="gte")
    end_value = NumberFilter(field_name="value", lookup_expr="lte")

    class Meta:
        model = Operation
        fields = ['operation_type', 'payment_method']