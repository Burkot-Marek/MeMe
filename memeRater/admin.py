from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Meme)
@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    fields = ('title', 'picture', 'dateOfBirth', 'dateOfDeath', 'description','public',)
    list_display = ('title', 'created', 'dateOfBirth', 'dateOfDeath', )
    list_filter = ('title', 'created', 'dateOfBirth', 'dateOfDeath')
    search_fields = ('title', 'description',)


admin.site.register(Comment)
# admin.site.register(MemeClass)