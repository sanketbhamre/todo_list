from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView

from Todo.todo.todo_list.models import List
from .serializers import ListSerializer


@api_view(['GET', ])
def api_detail_list_view(request, slug):
    try:
        to_list = List.objects.get(slug=slug)
    except List.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ListSerializer(to_list)
        return Response(serializer.data)
