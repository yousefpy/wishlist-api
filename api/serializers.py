from rest_framework import serializers
from items.models import Item
from django.contrib.auth.models import User


class AddedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ItemListSerializer(serializers.ModelSerializer):
    wish_for = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
        view_name = 'item-detail',
        lookup_field = 'id',
        lookup_url_kwarg = 'item_id'
    )
    added_by = AddedBySerializer()
    class Meta:
        model = Item
        fields = ['image', 'added_by', 'name', 'detail', 'wish_for']
    
    def get_wish_for(self, obj):
        return "Wish for %s"%(obj.name)

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'





    