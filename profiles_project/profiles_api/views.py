from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer
    #format=True returns a list of API view
    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
        
        return Response({'messege': 'Hello', 'an_apibiew': an_apiview})

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            #fString 문자열에 변수를 추가할 수 있음
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pd=None):
        #업데이트에 사용 일부분만 업데이트를 원하면 patch를 사용해야함
        #put으로 일부분의 정보만 주었을 시 나머지는 default로 업데이트됨
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        #request에 있는 정보만 업데이트 된다
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        #삭제할 떄 사용
        return Response({'method':'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    #Test API ViewSEt

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        #Return a gello message
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})


    def create(self, request):
        #Create a new hello message
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        #Handle getting an object bby its ID
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        #Handle updaing an object
        return Response({'http_method': 'UPDATE'})

    def partial_update(self, request, pk=None):
        #Handle updaing part of an object
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        #Handle removing an object
        return Response({'http_method': 'DELETE'})


class UserProfileViewset(viewsets.ModelViewSet):
    #Handle creating and updating profiles
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )


class UserLoginApiView(ObtainAuthToken):
    #Handle creating user authentication tokens
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES