from rest_framework.views import APIView
from rest_framework.response import Response # when Django framework call APIView it exprected to return the standard response object
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets # This is for importing the view set
from rest_framework.authentication import TokenAuthentication # it used for the user to authenticate themserlfes with the API
from profiles_api import permissions
from profiles_api import models



# This class allow us to define an application logic for the endpoint
class HelloApiView(APIView):
    """Test API View"""
    # This configure our API view to have the serializer class that is created in serializer.py.
    serializer_class = serializers.HelloSerializer
    # This is used when a client sends a GET request to your endpoint
    def get(self, request, format=None):
        """Resturns a list of APIView features"""
        an_apiview = [
        'Uses HTPP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Give you the most control over you application logic',
        'Is mapped manually to URLS',
        ]
        # in order to convert it to Json the data should be a list or distionary.
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    # This post function is used when a client wants to send data to the server:
    def post(self, request):
        """Create a hello message with our name"""
        Serializer = self.serializer_class(data=request.data)
                    #self.serializer it comes with APIView that retrieve configured serializer in APIView.
        # This is how to see if the serializer is valide
        if Serializer.is_valid():
            name = Serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                Serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    # HTTP PUT request is often used for update an object, replacing
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    # HTTP PATCH request update but only update the fields that provided in the request like last name.
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})



# Here is the class for viewset:
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    # Here we can specify the serializer:
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    # This is the create function:
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        # Here to validate the serializer:
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    # This is the retrieve function:
    def retrieve(self, request, pk=None): #pk means primary key.
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Handle updating part of an object """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})




# Creating new models viewset:
#use a model view set is you connect it up to a
#serializer class just like you would a regular view set and you provide a query,
#set to the model view set so it knows which objects in the database are going,
#to be managed through this view set,
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating proiles"""
    # assigning the serializer class:
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) # The comma is to be created as Tuble.
    permission_classes = (permissions.UpdateOwnProfile,)
