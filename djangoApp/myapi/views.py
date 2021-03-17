from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import CountriesSerializer
from .models import Countries


class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all().order_by('country_name')
    serializer_class = CountriesSerializer