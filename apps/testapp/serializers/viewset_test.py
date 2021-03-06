from rest_framework import serializers
from apps.testapp.models import Modifier


class ModifierSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=255)
    modifier = serializers.CharField(max_length=127)
    default_value = serializers.FloatField()

    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.modifier = validated_data.get('modifier', instance.modifier)
        instance.default_value = validated_data.get('default_value', instance.default_value)
        return instance

    def create(self, validated_data):
        return Modifier(**validated_data)
