from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list(dictionairy) of APIView feautures"""
        an_apiview=[
            'Lalalalala',
            'Hello',
            'John',
        ]

        return Response({'message':'Hello World','an_apiview':an_apiview})
