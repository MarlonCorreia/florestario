from django.http.response import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from author.serializers import AuthorSerializer
from author.models import Author


class AuthorList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, requets):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True).data
        return Response(serializer)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class AuthorView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author).data
        return Response(serializer)
    
    def delete(self, request, pk):
        author = self.get_object(pk)
        author.delete()
        return Response(status=200)
    
    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def get_object(self, pk):
        try:
            author = Author.objects.get(pk=pk)
            return author
        except Author.DoesNotExist:
            raise Http404

    