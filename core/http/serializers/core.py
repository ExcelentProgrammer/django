from common import serializers
from core.http.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', "desc", "image"]
