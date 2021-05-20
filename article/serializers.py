from django.db import models
from rest_framework import serializers
from article.models import Article
from author.models import Author

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        depth = 1
    
    def check_author_id(self, data):
        try:
            author_id = data["author"]
            if Author.objects.filter(id=author_id).exists():
                return True
            raise Exception
        except:
            raise serializers.ValidationError("author field not set or invalid")