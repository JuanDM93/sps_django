from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend, filterset

from users.permissions import IsAdminOrReadOnly
from customers.models import Customer
from customers.api.serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'username'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']
