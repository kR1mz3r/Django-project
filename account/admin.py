from django.contrib import admin
from .models import CustomUser

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'middle_name', 'photo', 'department', 'role', 'user_id')
admin.site.register(CustomUser, UserAdmin)



