# -*- coding: utf-8 -*-
from rest_framework import serializers
from apps.tracking.models import LogCategory, BudgetLog


class LogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogCategory
        fields = ('id', 'name', 'key',)


class BudgetLogSerializer(serializers.ModelSerializer):

    category = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=LogCategory.objects.all())

    def create(self, validated_data):
        return BudgetLog.objects.create(
            user=self.context['request'].user,
            **validated_data
        )

    class Meta:
        model = BudgetLog
        fields = ('id', 'title', 'amount', 'date', 'category',)