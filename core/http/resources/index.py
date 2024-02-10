from import_export import resources

from core.http.models import Post


class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ('id', 'title', 'desc')
