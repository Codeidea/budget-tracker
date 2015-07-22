# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = (
    url(regex=r'^tracking$', view=views.TrackingExpenseCreateView.as_view(), name='tracking_expense'),
    url(regex=r'^logs$', view=views.LogEntriesListAPI.as_view({'get': 'list'}), name='logs'),
    url(regex=r'^log_categories$', view=views.LogCategoriesListAPI.as_view(), name='log_categories'),
)