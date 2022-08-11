from rest_framework import viewsets

from book_copy.models import BookCopy

from .serializers import BookCopySerializer

# Create your views here.


class BookCopyViewset(viewsets.ModelViewSet):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return BookCopySerializer
        else:
            return BookCopySerializer
