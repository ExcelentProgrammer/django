from modeltranslation.translator import TranslationOptions


class PostTranslationOption(TranslationOptions):
    fields = ("title", "desc",)
