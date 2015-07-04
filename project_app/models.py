from decimal import Decimal

from django.db import models
from client_app.models import Client

# Create your models here.


class Project(models.Model):
    client = models.ForeignKey(Client)
    name = models.CharField(max_length=150)
    technology_used = models.CharField(max_length=150, null=True, blank=True)
    cost_per_hour = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('0.00'))
    start_date = models.DateField(auto_now_add=True)
    time_spent = models.IntegerField(null=True, blank=True, help_text="Time Spent in Hours")
                                       
    def __unicode__(self):
        return u'{} - {}'.format(self.name, self.client.user.first_name or self.client.user.email or 'Client')
