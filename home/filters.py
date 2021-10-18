from django.db.models import fields
import django_filters
from django_filters.filters import DateFromToRangeFilter, DateRangeFilter, ModelChoiceFilter, ModelMultipleChoiceFilter, NumberFilter
from .models import *
from django_filters import DateFilter


class OperationsFilter(django_filters.FilterSet):
    # operation1 = Operation.objects.last()
    # clientName = operation1.client.name
    # clientVehicles = Vehicle.objects.filter(owners__name=clientName)

    date_range = DateFromToRangeFilter(field_name='date') 
        # ,widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))
    # vehicle = ModelChoiceFilter(queryset=clientVehicles)
    start_value = NumberFilter(field_name="value", lookup_expr="gte")
    end_value = NumberFilter(field_name="value", lookup_expr="lte")

    class Meta:
        model = Operation
        fields = ['operation_type', 'payment_method']