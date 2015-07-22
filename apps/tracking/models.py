from django.db import models
from apps.users.models import User
from django.utils import timezone

class LogCategory(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=50)

    def __unicode__(self):
        return self.key

class BudgetLog(models.Model):

    user = models.ForeignKey(User)

    title = models.CharField(max_length=255)
    category = models.ForeignKey(LogCategory, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField()

    created_at = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return self.title

