from rest_framework import serializers
from .models import Blog, BlogCategory



class BlogSerializerForCategory(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description')


class BlogCategorySerializer(serializers.ModelSerializer):
    blogs = BlogSerializerForCategory(many=True)
    class Meta:
        model = BlogCategory
        fields = ('id', 'category_title', 'blogs')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ( 'category_title',)


class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many = True)
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'categories')

