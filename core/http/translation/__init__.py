from modeltranslation.translator import translator

from core.http.models import Post
from core.http.translation.core import PostTranslationOption

translator.register(Post, PostTranslationOption)
