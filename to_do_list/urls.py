from django.urls import include, path

from rest_framework import routers

from .views import ToDoListItemViewSet

router = routers.DefaultRouter()
router.register(r'', ToDoListItemViewSet)

urlpatterns = [
   path('', include(router.urls)),
]