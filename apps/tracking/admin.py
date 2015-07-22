from django.contrib import admin
from .models import LogCategory, BudgetLog
# Register your models here.
admin.site.register(LogCategory)
admin.site.register(BudgetLog)