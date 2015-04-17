from django.contrib import admin

from .models import Package

# Register your models here.
class PackageAdmin(admin.ModelAdmin):
    fields = ['name','program','description','cover','author','upstream','version']

admin.site.register(Package,PackageAdmin)
