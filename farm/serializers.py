from rest_framework import serializers
from .models import Sheep

class SheepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheep
        fields = '__all__'