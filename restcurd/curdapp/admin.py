from django.contrib import admin
from . models import Studentmodel

@admin.register(Studentmodel)
class StudentAdminmodel(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
