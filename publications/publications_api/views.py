from rest_framework import mixins, permissions, viewsets

from .models import Publication
from .serializers import PublicationSerializer

from users_api.permissions import IsAuthorOrReadOnly


class PublicationsViewSet(viewsets.ModelViewSet):
    serializer_class = PublicationSerializer
    permission_classes = (permissions.AllowAny, IsAuthorOrReadOnly,)    

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Publication.objects.all()
            is_private = self.request.query_params.get('private', False)
            if is_private:
                queryset = queryset.filter(is_public=False)
            return queryset
        return Publication.objects.filter(is_public=True)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
