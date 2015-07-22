# -*- coding: utf-8 -*-
import django_filters
from apps.tracking.models import BudgetLog


class DateFilter(django_filters.FilterSet):

    date__lt = django_filters.DateFilter(name='date', lookup_type='lt')
    date__gt = django_filters.DateFilter(name='date', lookup_type='gt')

    class Meta:
        model = BudgetLog
        fields = ('date',)
