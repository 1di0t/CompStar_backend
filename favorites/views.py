from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Favorite
from .serializers import FavoriteSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(user=user).select_related(
            'region', 'sub_region', 'category'
        )

    def perform_create(self, serializer):
        # automatically assign the current user when creating a favorite
        serializer.save(user=self.request.user)