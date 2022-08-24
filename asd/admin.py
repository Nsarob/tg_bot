from csv import list_dialects
from django.contrib import admin
from .models import Profile,Message 
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "external_id")

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "profile", "text", 'created_at')

    #def get_queryset(self, request):
        #return