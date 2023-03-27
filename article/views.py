from rest_framework import viewsets, filters
from article.models import Article, Category, Tag
from article.permissions import IsAdminUserOrReadOnly
from article.serializers import ArticleSerializer, CategorySerializer, CategoryDetailSerializer, TagSerializer

"""GET:用户发请求-->Django根据url找到viewset-->viewset调用父类的list()方法,返回Article的列表"""
"""POST:用户发请求-->Django根据url找到viewset-->将请求转为Python对象-->viewset调用父类的create()方法,创建并保存"""


class ArticleViewSet(viewsets.ModelViewSet):
    """文章视图集"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    # 模糊搜索
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Category.objects.all()

    # serializer_class = CategorySerializer

    def get_serializer_class(self):
        # 如果action是list,返回包含全部的序列化器
        if self.action == 'list':
            return CategorySerializer
        else:
            # 返回只包含title和url的简介序列化器
            return CategoryDetailSerializer


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
