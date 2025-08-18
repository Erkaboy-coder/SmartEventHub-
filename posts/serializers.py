# events/serializers.py
from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # username ko‘rinadi

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']