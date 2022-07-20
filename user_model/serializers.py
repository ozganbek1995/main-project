from rest_framework import serializers

from user_model.models import User
from api.models import Shop

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'img')


class ShopSerializer(serializers.ModelSerializer):
    viloyat = serializers.IntegerField()
    tuman = serializers.IntegerField()
    
    class Meta:
        model = Shop
        fields = ('name', 'description', 'image', 'password', 'viloyat', 'tuman')


