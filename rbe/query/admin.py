from django.contrib import admin

from .models import Rice

# Register your models here.
class RiceAdmin(admin.ModelAdmin):
    fields = ['name','program','description','cover','pic1','pic2','pic3','pic4','author','upstream','version']

admin.site.register(Rice,RiceAdmin)
