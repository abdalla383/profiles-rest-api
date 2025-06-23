from rest_framework.views import APIView
from rest_framework.response import Response # it used to resturn responses from the API

# This class allow us to define an application logic for the endpoint
class HelloApiView(APIView):
    """Test API View"""
    # is it used to retrieve the list of element.
    def get(self, request, format=None):
        """Resturns a list of APIView features"""
        an_apiview = [
        'Uses HTPP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Give you the most control over you application logic',
        'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
