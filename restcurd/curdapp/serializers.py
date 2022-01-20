from rest_framework import serializers
from . models import Studentmodel

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Studentmodel
        fields = ['id','name','roll','city']