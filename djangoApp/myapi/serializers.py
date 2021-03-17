from rest_framework import serializers  
from .models import Countries

class CountriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Countries
        fields=("id",'country_name', 'capital', 'population')