from django.contrib import admin
from .models import Chat, Message

class MessageAdmin(admin.ModelAdmin):    #mit dieser Klasse wird für die Adminseite bestimmt was angezeigt werden soll Naneskonvention = ImportKlasse + Admin
    fields = ('chat','text','created_at', 'author', 'receiver')    
    list_display = ('created_at', 'author', 'text', 'receiver')    
    search_fields = ('text',)

# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
