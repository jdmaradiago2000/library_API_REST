from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import UserLibrary
from .serializers import UserSerializer


# Create your views here.
class UserLibraryViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserLibrary.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return UserSerializer
        else:
            return UserSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [AllowAny]
            return [permission() for permission in self.permission_classes]

        else:
            self.permission_classes = [IsAuthenticated]
            return [permission() for permission in self.permission_classes]
