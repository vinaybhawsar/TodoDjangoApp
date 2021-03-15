"""todo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path

from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# REST API Schema
schema_view = get_schema_view(
   openapi.Info(
      title="TODO APP API",
      default_version='v1',
      description="TODO APP API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@todo.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

excluded_url = [
    # Admin panel URL
    path('admin/', admin.site.urls),
    # Custom App URLs
    path('api/v1/', include('todo_manager.urls')),
]

urlpatterns = excluded_url + [
    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger')),
    # Swagger Schema in JSON or YAML format
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(), name='schema-json'),
    # ReDoc UI
    re_path(r'^redoc/$', schema_view.with_ui('redoc'),
            name='schema-redoc'),
]
