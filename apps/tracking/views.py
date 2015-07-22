from django.shortcuts import render
from rest_framework import views, serializers, generics, filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.tracking.filters import DateFilter
from apps.tracking.serializers import BudgetLogSerializer, LogCategorySerializer
from .models import BudgetLog, LogCategory
import django_filters


class TrackingExpenseCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BudgetLogSerializer


class LogEntriesListAPI(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)

    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = DateFilter
    filter_fields = ('date',)

    serializer_class = BudgetLogSerializer

    def get_queryset(self):
        return BudgetLog.objects.filter(user=self.request.user).order_by('-date')


class LogCategoriesListAPI(generics.ListCreateAPIView):
    queryset = LogCategory.objects.all()
    serializer_class = LogCategorySerializer
    permission_classes = (IsAuthenticated,)