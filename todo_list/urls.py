from django.conf.urls import *
from .views import todo_list, todo_detail, ListAPIView, TodoDetail, GenericAPIView
from django.urls import path

urlpatterns = [
    #path('', views.home, name="home"),
    #path('todo/', views.todo_list, name='todo_list'),
    #path('detail/<int:pk>/', todo_detail, name='todo_detail'),
    path('todo/', ListAPIView.as_view()),
    path('detail/<int:id>/', TodoDetail.as_view()),
    path('generic/todo/<int:id>/', GenericAPIView.as_view()),
    #path('delete/<list_id>', views.delete, name="delete"),
    #path('cross_off/<list_id>', views.cross_off, name="cross_off"),
    #path('uncross/<list_id>', views.uncross, name="uncross"),

]
