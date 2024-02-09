from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets

from common.env import env
from core.http.models import Post
from core.http.serializers import PostSerializer


class PostListView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @method_decorator(cache_page(env("CACHE_TIME")))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
