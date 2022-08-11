from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import ShelfBookCopy
from .serializers import ShelfSerializer


# Create your views here.
class ShelfViewSet(viewsets.ModelViewSet):
    queryset = ShelfBookCopy.objects.all()
    serializer_class = ShelfSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ["shelf__category", "shelf__section", "sub_section"]

    search_fields = {"shelf__category", "shelf__section", "sub_section"}
