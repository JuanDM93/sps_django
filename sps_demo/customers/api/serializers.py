from rest_framework.serializers import ModelSerializer
from customers.models import Customer
 
 
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'username', 'email',
        ]
