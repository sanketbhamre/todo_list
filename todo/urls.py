from django.contrib import admin
from django.conf.urls import *
from todo_list import views
from django.urls import path, include

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
'''
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
'''
urlpatterns = [
    path('', include('todo_list.urls')),
    path('admin/', admin.site.urls),
    #url(r'^api/', include('todo_list.urls')),
    #path('accounts/', include('accounts.urls')),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('api/accounts', include(('accounts.api.urls','accounts_api'), namespace='accounts_api')),


]
