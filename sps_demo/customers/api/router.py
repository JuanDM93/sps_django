from rest_framework.routers import DefaultRouter
from customers.api.views import CustomerViewSet


customers_router = DefaultRouter()
customers_router.register(
    prefix='customers', basename='customers',
    viewset=CustomerViewSet
)
