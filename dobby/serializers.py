__author__ = 'shivamgupta'

from rest_framework import serializers
from dobby.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'href', 'imghref', 'price', 'origprice')
