"""django_admin URL Configuration

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
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from platform_auth.views import AuthUserViewSet

userRouter = DefaultRouter()
userRouter.register(r'', AuthUserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/dj/todolists/', include('to_do_list.urls')),
    path('api/dj/users/', include(userRouter.urls)),
    path('api/dj/platform_users/', include('platform_auth.urls')),
    path('api/dj/auth/', include('rest_framework.urls')),
    path('api/dj/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/dj/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


