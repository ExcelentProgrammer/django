from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from core.http.forms.admin import PostAdminForm
from core.http.models import Post, User, SmsConfirm, FrontendTranslation
from core.http.resources import FrontendTranslationResource
from core.http.resources.base import PostResource


class PostAdmin(TabbedTranslationAdmin, ImportExportModelAdmin):
    fields: tuple = ('title', "desc", "image")
    resource_classes: list = [PostResource]
    search_fields: list = ['title', 'desc']
    list_filter = ['title']
    required_languages: tuple = ('uz',)
    form = PostAdminForm


class CustomUserAdmin(UserAdmin):
    list_display = ['phone', "first_name", "last_name"]


class FrontendTranslationAdmin(TabbedTranslationAdmin, ImportExportModelAdmin):
    fields: tuple = ("key", "value")
    required_languages: tuple = ('uz',)
    list_display = ["key", "value"]

    resource_classes = [FrontendTranslationResource]


admin.site.register(FrontendTranslation, FrontendTranslationAdmin)
admin.site.register(SmsConfirm)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Post, PostAdmin)