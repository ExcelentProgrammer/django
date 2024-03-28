################################
# Django django-import-export resources
################################


from import_export import resources

from core.http.models import Post, FrontendTranslation


class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ('id', 'title', 'desc')


class FrontendTranslationResource(resources.ModelResource):
    class Meta:
        model = FrontendTranslation
        fields = ('id', 'key', "value")
