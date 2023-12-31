from django.contrib import admin
from .models import Commune, Employee, Service, Travailler

admin.site.register(Commune)
admin.site.register(Employee)
admin.site.register(Service)
admin.site.register(Travailler)
