from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from core.http.models import Post


class PostAdmin(TabbedTranslationAdmin):
    fields = ('title', "desc", "image")
    required_languages = ('uz',)


admin.site.register(Post, PostAdmin)
