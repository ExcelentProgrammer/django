from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from core.http.models import Post
from core.http.resources.index import PostResource


class PostAdmin(TabbedTranslationAdmin, ImportExportModelAdmin):
    fields = ('title', "desc", "image")
    resource_classes = [PostResource]
    required_languages = ('uz',)


admin.site.register(Post, PostAdmin)
