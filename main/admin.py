from django.contrib import admin
from .models import MLModel, DataFile

class MLModelAdmin(admin.ModelAdmin):
    list_display = ('model_id', 'created_by', 'created_at')

class DataFileAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'filename', 'uploaded_by', 'uploaded_at')

admin.site.register(MLModel, MLModelAdmin)
admin.site.register(DataFile, DataFileAdmin)
