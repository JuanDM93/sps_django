from rest_framework.routers import DefaultRouter
from accounts.api.views import AccountViewSet


accounts_router = DefaultRouter()
accounts_router.register(
    prefix='accounts', basename='accounts',
    viewset=AccountViewSet
)