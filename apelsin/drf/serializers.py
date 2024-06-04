from rest_framework import serializers
from .models import MenuItem, Contact

class MenuItemSerilarizer(serializers.ModelSerializer):
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']
        extra_kwargs = {
            'price':{'min_value':2},
            'inventory':{'min_value':0}
        }

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'