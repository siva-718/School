from django.contrib import admin
from .models import Department,Order,Course,Material

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Department,DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','department']
    list_editable = ['department']
admin.site.register(Course,CourseAdmin)