from rest_framework import serializers
from article.models import Article


# class ArticleListSerializer(serializers.Serializer):
#     """序列化器"""
#     id = serializers.CharField(read_only=True)
#     title = serializers.CharField(max_length=100, allow_blank=True)
#     body = serializers.CharField(allow_blank=True)
#     created = serializers.DateTimeField()
#     updated = serializers.DateTimeField()

class ArticleListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='article:detail')

    class Meta:
        model = Article
        fields = [
            # 'id',
            'url',
            'title',
            'body',
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
