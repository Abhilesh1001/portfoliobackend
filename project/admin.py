from django.contrib import admin
from .models import Project

# Register your models here.
@admin.register(Project)
class ModdelAdminProject(admin.ModelAdmin):
    list_display =['project_id','name','desc','image','skil','githubLinkFrontend','githubLinkBAckend','backendLink','frontendLink']