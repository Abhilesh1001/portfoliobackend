from django.contrib import admin
from .models import Project,Message

# Register your models here.
@admin.register(Project)
class ModdelAdminProject(admin.ModelAdmin):
    list_display =['project_id','name','desc','image','skil','githubLinkFrontend','githubLinkBAckend','backendLink','frontendLink']

@admin.register(Message)
class ModelAdminMessage(admin.ModelAdmin):
    list_display=['message_id','name','email','message']