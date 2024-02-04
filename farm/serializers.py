from rest_framework import serializers
from .models import Sheep, Sex
from enumchoicefield import EnumChoiceField

class SheepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheep
        fields = '__all__'
    id = serializers.UUIDField(read_only=True)
    sex = EnumChoiceField(enum_class=Sex)