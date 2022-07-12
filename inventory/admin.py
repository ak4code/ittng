from django.contrib import admin
from .models import Storage, Organization


class StorageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Storage, StorageAdmin)
admin.site.register(Organization)
