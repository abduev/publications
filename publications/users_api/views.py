from rest_framework import mixins, permissions, viewsets

from .models import CustomUser
from .serializers import CustomUserSerializer


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny, )
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
