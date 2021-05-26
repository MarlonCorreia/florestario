from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from article.models import Article, Author
from article.serializers import ArticleSerializer, AnonArticleSerializer


class ArticleList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        category = request.query_params.get('category')
        if category:
            articles = Article.objects.filter(category=category)
        else:
            articles = Article.objects.all()

        if is_anon(request):
            serializer = AnonArticleSerializer(articles, many=True).data
        else:
            serializer = ArticleSerializer(articles, many=True).data        

        return Response(serializer)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid() and serializer.check_author_id(request.data):
            serializer.save(author=Author.objects.get(id=request.data["author"]))
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
            

class ArticleView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        article = self.get_object(pk)

        if is_anon(request):
            serializer = AnonArticleSerializer(article).data
        else:
            serializer = ArticleSerializer(article).data

        return Response(serializer)       

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=200)
    
    def put(self, request, pk):
        article = self.get_object(pk)

        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
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