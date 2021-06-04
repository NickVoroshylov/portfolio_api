from rest_framework import filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from portfolios.models import Picture
from portfolios.serializers import PictureSerializer, PictureDetailSerializer


class PictureViewSet(ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureDetailSerializer
    #permission_classes = [IsAuthenticated]
    serializer_action_classes = {
        'list': PictureSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
