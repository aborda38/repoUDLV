from rest_framework import viewsets
from .models import librosmodel
from .serializer import LibrosSerializer



class LibrosViewSet (viewsets.ModelViewSet):
    queryset = librosmodel.objects.all()
    serializer_class = LibrosSerializer