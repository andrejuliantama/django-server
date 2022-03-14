from rest_framework import serializers

from .models import ToDoListItem


class ToDoListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoListItem
        fields = ('uuid', 'status', 'content', 'start_date', 'end_date', 'updated_at')
