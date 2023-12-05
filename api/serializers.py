from rest_framework import serializers
from .models import Advert


class AdvertSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    created = serializers.DateTimeField(format="%d.%m.%Y", read_only=True)

    class Meta:
        model = Advert
        fields = '__all__'
        deferred_fields = ['city', 'category']
