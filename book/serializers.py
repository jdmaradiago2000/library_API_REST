from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Author


#      depth = 1


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        fields = "__all__"
        model = Book


#      depth = 1
class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Book


class ReadBookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Book
