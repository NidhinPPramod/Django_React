from django.contrib import admin

from .models import DetailsModel

# Register your models here.

class DetailsModelAdmin(admin.ModelAdmin):
    list_display=('name','age','city') 

admin.site.register(DetailsModel,DetailsModelAdmin)
