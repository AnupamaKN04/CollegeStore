from django.contrib import admin

# Register your models here.
from . models import Department,Product
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Department,DepartmentAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','available','created','updated']
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)