from rest_framework.viewsets import ModelViewSet

from accounts.models import Profile
from accounts.serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
