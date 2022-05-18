from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from references.models import Reference
from references.serializers import ReferenceSerializer


class ReferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ReferenceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Reference.objects.all()
