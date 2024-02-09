from rest_framework import viewsets
from faunatrack.models import Espece
from faunatrack.serializers import EspeceSerializer
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class EspeceViewSet(viewsets.ModelViewSet):
    queryset = Espece.objects.all()
    serializer_class = EspeceSerializer
    permission_classes = [IsAuthenticated]



class ExampleView(APIView):
    # authentication_classes = [TokenAuthentication]
    # authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user.email),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)