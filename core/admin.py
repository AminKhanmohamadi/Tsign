from django.contrib import admin
from core.models import File, Folder
# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['name' , 'file_type' , 'size']

class FileAdminInline(admin.TabularInline):
    model = File
    extra = 1

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    inlines = [FileAdminInline]
