from django.contrib import admin
from .models import AwardImageUpload, FileUpload

admin.site.register(FileUpload)
admin.site.register(AwardImageUpload)
