from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import ListSerializer
from rest_framework.parsers import JSONParser
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import response, JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import responses, Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BaseAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

'''
class RegisterUser(APIView):
    def post(self, request):
        import pdb
        pdb.set_trace()
        # data = request.data
        # name = data.get('name')
        # password = data.get('password')
        # user = User(name=name)
        # user.set_password(password)
        # user.save()
        # return Response({"Data saved Successfully"}, status=status.HTTP_200_OK)
        return Response('Hi', status=status.HTTP_200_OK)
'''


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ListSerializer
    queryset = List.objects.all()
    lookup_field = 'id'

    # authentication_classes = [BaseAuthentication, SessionAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class ListAPIView(APIView):
    def get(self, request):
        todo = List.objects.all()
        serializer = ListSerializer(todo, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    def get_object(self, id):
        try:
            return List.objects.get(id=id)
        except List.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        todo_l = self.get_object(id)
        serializer = ListSerializer(todo_l)
        return Response(serializer.data)

    def put(self, request, id):
        todo_l = self.get_object(id)
        serializer = ListSerializer(todo_l, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        todo_l = self.get_object(id)
        todo_l.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todo = List.objects.all()
        serializer = ListSerializer(todo, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def todo_detail(request, pk):
    try:
        todo_l = List.objects.get(pk=pk)

    except List.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ListSerializer(todo_l)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = ListSerializer(todo_l, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo_l.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ListSerializer(todo_l, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    # import pdb
    # pdb.set_trace()
    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, 'Item has been added to the list')
            return render(request, 'pages/home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'pages/home.html', {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'Item deleted successfully')
    return redirect('home')


def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')
