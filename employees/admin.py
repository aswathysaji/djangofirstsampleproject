from django.contrib import admin
from .models import Employee
from .models import Available_jobs
# Register your models here.
 
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email_id','phone_number']

@admin.register(Available_jobs)
class Available_jobsAdmin(admin.ModelAdmin):
    list_display=['name']