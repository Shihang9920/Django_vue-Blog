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

# def get_queryset(self):
#     queryset = self.queryset
#     username = self.request.query_params.get('username', None)
#     if username is not None:
#         queryset = queryset.filter(author__username=username)
#     return queryset

# def test(self):
#     request = Request(self.request)
#     print(request.user)
#     print(list(request.query_params.items()))
#     print(request.auth)
#     print(request.method)
#
# def dispatch(self, request, *args, **kwargs):
#     self.test()
#     return super().dispatch(request, *args, **kwargs)

# @api_view(['GET', 'POST'])
# def article_list(request):
#     permission_class = [IsAuthenticated]
#     if request.method == 'GET':
#         # 取出所有文章的queryset
#         articles = Article.objects.all()
#         # 将queryset的数据序列化
#         serializer = ArticleListSerializer(articles, many=True)
#         # 将序列化的数据以JSON的形式返回
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ArticleListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleList(generics.ListCreateAPIView):
#     permission_classes = [IsAdminUserOrReadOnly]
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


# def get(self, request):
#     articles = Article.objects.all()
#     serializer = ArticleListSerializer(articles, many=True, context={'request': request})
#     return Response(serializer.data)


# class ArticleDetails(APIView):
#     permission_classes = [IsAdminUserOrReadOnly]
#
#     @staticmethod
#     def get_object(pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except:
#             raise Http404
#
#     def get(self, request, pk):
#         article = self.get_object(pk)
#         serializer = ArticleDetailSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         article = self.get_object(pk)
#         serializer = ArticleDetailSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAdminUserOrReadOnly]
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
