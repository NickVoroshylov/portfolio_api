from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer

from portfolios.models import Picture


class PictureSerializer(ModelSerializer):

    portfolio__name = ReadOnlyField(source='portfolio.name')

    class Meta:
        model = Picture
        fields = ('portfolio__name', 'name', 'description', 'created')


class PictureDetailSerializer(ModelSerializer):
    class Meta:
        model = Picture
        fields = ('name',)
