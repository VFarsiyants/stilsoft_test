from rest_framework import viewsets

from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

