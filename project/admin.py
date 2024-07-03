from django.contrib import admin
from .models import Project, Task

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('created_at',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'assigned_to', 'description', 'files', 'updated_files', 'updated_description',
                    'created_at', 'updated_at')
    list_display_links = ('id', 'project')
    search_fields = ('project',)
    list_filter = ('created_at', 'updated_at')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)




