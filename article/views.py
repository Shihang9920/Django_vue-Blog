from article.models import Article
from django.http import JsonResponse, Http404
from article.serializers import ArticleListSerializer, ArticleDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from article.permissions import IsAdminUserOrReadOnly


# Create your views here.


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


class ArticleList(generics.ListAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

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


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
