from rest_framework.views import APIView
from rest_framework.response import Response # when Django framework call APIView it exprected to return the standard response object
from rest_framework import status
from profiles_api import serializers


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
