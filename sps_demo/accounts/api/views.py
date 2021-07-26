from re import I
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsAdminOrReadOnly
from accounts.models import Account
from accounts.api.serializers import AccountSerializer


class AccountViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    lookup_field = 'account_id'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['account_id',]