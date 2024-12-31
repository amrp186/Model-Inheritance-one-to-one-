from django.contrib import admin
from .models import Aadhar
from .models import Students

# Register your models here.
@admin.register(Aadhar)
class AadharAdmin(admin.ModelAdmin):
    list_display = ['aadhar']

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stu_name','stu_email','stu_contact','aadhar_no']

