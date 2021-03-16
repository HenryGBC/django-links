from django.contrib import admin
from .models import Links
# Register your models here.

@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    pass
