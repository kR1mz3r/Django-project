from django.contrib import admin
from .models import Message

class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'content', 'timestamp')
    list_display_links = ()
    search_fields = ()
admin.site.register(Message, ChatAdmin)


