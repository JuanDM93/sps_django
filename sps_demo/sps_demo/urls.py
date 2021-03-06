"""sps_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from customers.api.router import customers_router
from accounts.api.router import accounts_router


# Documentation Schema
schema_view = get_schema_view(
    openapi.Info(
        title='SPS API',
        default_version='v1',
        description='Basic Django API Demo for SPSolutions',
        contact=openapi.Contact('juan_dm93@hotmail.com'),
        license=openapi.License('MIT Licence'),
    ),
    public=True
)

# Main Paths
urlpatterns = [
    # Management
    path('admin/', admin.site.urls),

    # Services
    path('api/', include('users.api.router')),
    path('api/', include(customers_router.urls)),
    path('api/', include(accounts_router.urls)),

    # Docs
    path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
