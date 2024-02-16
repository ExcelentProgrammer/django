from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from core.http.models import Post, User, SmsConfirm
from core.http.resources.index import PostResource


class PostAdmin(TabbedTranslationAdmin, ImportExportModelAdmin):
    fields: tuple = ('title', "desc", "image")
    resource_classes: list = [PostResource]
    required_languages: tuple = ('uz',)


class CustomUserAdmin(UserAdmin):
    list_display = ['phone', "first_name", "last_name"]


admin.site.register(SmsConfirm)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Post, PostAdmin)
