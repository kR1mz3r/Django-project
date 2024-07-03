from django.contrib import admin
from base.models import BaseProjectTask

class ArchiveAdmin(admin.ModelAdmin):
    list_display = ('project', 'description')
    filter_horizontal = ('task',)
    search_fields = ('project',)

admin.site.register(BaseProjectTask, ArchiveAdmin)
