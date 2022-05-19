from django.contrib import admin

from references.models import Reference


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ("label", "kind", "file")
