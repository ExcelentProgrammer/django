from rest_framework import viewsets

from core.http.models import Post
from core.http.serializers import PostSerializer
from core.http.tasks import my_task


class PostListView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs):
        dsd
        return super().dispatch(request, *args, **kwargs)
