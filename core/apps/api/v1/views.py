from rest_framework.generics import ListAPIView

from core.http.models import Post
from core.http.serializers import PostSerializer


class PostListView(ListAPIView):
    queryset: object = Post.objects.all()
    serializer_class = PostSerializer
