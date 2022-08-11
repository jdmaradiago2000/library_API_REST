from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import BasePermission

from .models import Book

# Create your views here.
from .serializers import BookSerializer, CreateBookSerializer


class IsLibrary(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):

        return bool(request.user and request.user.is_library)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    permission_classes = [IsLibrary]
    search_fields = {
        "title",
        "topic",
        "status",
        "category__name",
        "author__full_name",
        "created_at",
        "updated_at",
        "isbn",
    }

    def get_serializer_class(self):
        if self.action == "create":
            return CreateBookSerializer
        else:
            return BookSerializer
