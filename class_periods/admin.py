from django.contrib import admin
from .models import ClassPeriods, SessionTokens, StudentCheckin

# Register your models here.
admin.site.register(ClassPeriods)
admin.site.register(SessionTokens)
admin.site.register(StudentCheckin)
