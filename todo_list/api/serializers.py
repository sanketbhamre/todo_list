from rest_framework import serializers
from Todo.todo.todo_list.models import List


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['todo', 'completed']
