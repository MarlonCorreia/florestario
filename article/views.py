from django.http import Http404
from rest_framework.authtoken.models import Token

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from article.models import Article, Author
from article.serializers import ArticleSerializer, AnonArticleSerializer


class ArticleList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        articles = Article.objects.all()

        if is_anon(request):
            data = AnonArticleSerializer(articles, many=True).data
        else:
            data = ArticleSerializer(articles, many=True).data        

        return Response(data, status=200)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid() and serializer.check_author_id(request.data):
            serializer.save(author=Author.objects.get(id=request.data["author"]))
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
            

class ArticleView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        article = self.get_object(pk)

        if is_anon(request):
            data = AnonArticleSerializer(article)
        else:
            data = ArticleSerializer(article)

        return Response(data.data, status=200)       

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

def is_anon(request):
    if request.auth is None:
        return True
    return False