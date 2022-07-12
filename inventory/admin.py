from django.contrib import admin
from .models import Storage, Organization


class OrganizationInlines(admin.TabularInline):
    model = Organization
    extra = 1


class StorageAdmin(admin.ModelAdmin):
    inlines = (OrganizationInlines,)


admin.site.register(Storage, StorageAdmin)
admin.site.register(Organization)
