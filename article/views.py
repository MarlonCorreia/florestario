from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from article.models import Article, Author
from article.serializers import ArticleSerializer


class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        data = ArticleSerializer(articles, many=True).data
        return Response(data, status=200)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid() and serializer.check_author_id(request.data):
            serializer.save(author=Author.objects.get(id=request.data["author"]))
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
            

class ArticleView(APIView):
    def get(self, request, pk):
        article = self.get_object(pk)
        data = ArticleSerializer(article).data
        return Response(data, status=200)       

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=204)
    
    def put(self, request, pk):
        article = self.get_object(pk)

        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404 