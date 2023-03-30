from rest_framework import serializers
from article.models import Article, Category, Tag
from user_info.serializers import UserDescSerializer


class CategorySerializer(serializers.ModelSerializer):
    """序列化数据库中分类表"""
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created']


class ArticleCategoryDetailSerializer(serializers.ModelSerializer):
    """只序列化文章的url和title"""
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    class Meta:
        model = Article
        fields = [
            'url',
            'title'
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    article = ArticleCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created',
            'article',
        ]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleBaseSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    tag = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False,
        slug_field='text',
    )

    @staticmethod
    def validate_category_id(value):
        if not Category.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError('分类：{} 不存在', format(value))
        return value

    def to_internal_value(self, data):
        tags_data = data.get('tags')
        print(tags_data)
        if isinstance(tags_data, list):
            for text in tags_data:
                if not Tag.objects.filter(text=text):
                    Tag.objects.create(text=text)
        return super().to_internal_value(data)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializer(ArticleBaseSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {'body': {'write_only': True}}


class ArticleDetailSerializer(ArticleBaseSerializer):
    body_html = serializers.SerializerMethodField()
    toc_html = serializers.SerializerMethodField()

    def get_body_html(self, obj):
        return obj.get_md()[0]

    def get_toc_html(self, obj):
        return obj.get_md()[1]

    class Meta:
        model = Article
        fields = '__all__'
