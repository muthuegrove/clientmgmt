from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    user = models.ForeignKey(User)
    company_info = models.TextField()

    def __unicode__(self):
        return u'{}'.format(self.user.first_name or self.user.email or 'Client')
