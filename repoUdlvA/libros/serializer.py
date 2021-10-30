from .models import librosmodel
from rest_framework import serializers


class LibrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = librosmodel
        fields = '__all__'