from rest_framework import viewsets
from apps.testapp.models import Modifier
from apps.testapp.serializers.viewset_test import ModifierSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
class ModifierViewSet(viewsets.ViewSet):
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = Modifier.objects.all()
        serializer = ModifierSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Modifier.objects.all()
        modifier = get_object_or_404(queryset, pk=pk)
        serializer = ModifierSerializer(modifier)
        return Response(serializer.data)
