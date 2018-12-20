from rest_framework import serializers
from items.models import Item , FavoriteItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class UserFavSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = FavoriteItem
        fields = ['user']

class ItemListSerializer(serializers.ModelSerializer):
    liked_count = serializers.SerializerMethodField()

    added_by = UserSerializer()

    url_detail = serializers.HyperlinkedIdentityField(
        view_name = "detail-api",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
    class Meta:
        model = Item
        fields = ['name','url_detail','added_by','liked_count']

    def get_liked_count(self, obj):
        liked = FavoriteItem.objects.filter(item=obj)
        return liked.count()

class ItemDetailSerializer(serializers.ModelSerializer):
    liked_by = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['image', 'name', 'description','liked_by']

    def get_liked_by(self, obj):
        likers = FavoriteItem.objects.filter(item=obj)
        return UserFavSerializer(likers, many=True).data
