from rest_framework import serializers

from book.serializers import ReadBookSerializer
from users.serializers import MemberSerializer

from .models import BookCopy


class BookCopySerializer(serializers.ModelSerializer):
    book = ReadBookSerializer()
    member = MemberSerializer()

    class Meta:
        model = BookCopy
        fields = "__all__"


class BookcCreateCopySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = BookCopy
