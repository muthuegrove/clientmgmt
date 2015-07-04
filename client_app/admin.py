from django.contrib import admin
from .models import Client
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)
