from rest_framework import serializers

from models import Category, SubCategory


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('name', 'category')
        depth = 1