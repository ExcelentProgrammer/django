#####################
# Django model translation Resources
#####################

from modeltranslation.translator import TranslationOptions, translator

from core.http.models import Post, FrontendTranslation


class PostTranslationOption(TranslationOptions):
    fields = ("title", "desc",)


class FrontendTranslationOption(TranslationOptions):
    fields = ("value",)


translator.register(Post, PostTranslationOption)
translator.register(FrontendTranslation, FrontendTranslationOption)
