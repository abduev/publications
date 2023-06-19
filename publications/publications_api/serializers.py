from rest_framework import serializers

from .models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    pub_date = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = Publication
        fields = ('author', 'text', 'pub_date', 'is_public')
        extra_kwargs = {'is_public': {'write_only': True}}
