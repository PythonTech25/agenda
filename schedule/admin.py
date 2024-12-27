from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname',)
    list_display_links = 'id', 'firstname',
    list_per_page = 25
    ordering = '-id', 'firstname',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
