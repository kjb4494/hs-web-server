from rest_framework import viewsets
from apps.testapp.models import Modifier
from apps.testapp.serializers import ModifierSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.
class ModifierViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Modifier.objects.all()
        serializer = ModifierSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Modifier.objects.all()
        modifier = get_object_or_404(queryset, pk=pk)
        serializer = ModifierSerializer(modifier)
        return Response(serializer.data)
