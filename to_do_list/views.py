from rest_framework import viewsets

from .serializers import ToDoListItemSerializer
from .models import ToDoListItem


class ToDoListItemViewSet(viewsets.ModelViewSet):
   queryset = ToDoListItem.objects.all()
   serializer_class = ToDoListItemSerializer