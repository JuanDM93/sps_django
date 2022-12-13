from rest_framework.serializers import ModelSerializer
from accounts.api.serializers import AccountSerializer
from customers.models import Customer


class CustomerSerializer(ModelSerializer):
    accounts = AccountSerializer()

    class Meta:
        model = Customer
        fields = [
            'username', 'address', 'email', 'accounts'
        ]
