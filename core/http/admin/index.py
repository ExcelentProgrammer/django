from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from core.http.models import Post, User
from core.http.resources.index import PostResource


class PostAdmin(TabbedTranslationAdmin, ImportExportModelAdmin):
    fields: tuple = ('title', "desc", "image")
    resource_classes: list = [PostResource]
    required_languages: tuple = ('uz',)


class CustomUserAdmin(UserAdmin):
    def get_fieldsets(self, request, obj=None) -> tuple:
        return super().fieldsets + (
            (_("Custom Field"), {'fields': ("phone",)}),
        )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Post, PostAdmin)
