from modeltranslation.translator import translator

from core.http.models import Post, FrontendTranslation
from core.http.translation.index import PostTranslationOption, \
    FrontendTranslationOption

translator.register(Post, PostTranslationOption)
translator.register(FrontendTranslation, FrontendTranslationOption)
