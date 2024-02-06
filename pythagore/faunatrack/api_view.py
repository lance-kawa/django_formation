from rest_framework import viewsets
from faunatrack.models import Espece
from faunatrack.serializers import EspeceSerializer
from rest_framework import permissions

class EspeceViewSet(viewsets.ModelViewSet):
    queryset = Espece.objects.all()
    serializer_class = EspeceSerializer
    permission_classes = [permissions.IsAuthenticated]