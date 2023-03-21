from rest_framework import viewsets
from article.models import Article
from article.permissions import IsAdminUserOrReadOnly
from article.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

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
