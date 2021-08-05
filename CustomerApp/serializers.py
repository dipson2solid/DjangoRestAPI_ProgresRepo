from rest_framework import serializers
from CustomerApp.models import Customers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers 
        fields=('CustomerId','CustomerName')

