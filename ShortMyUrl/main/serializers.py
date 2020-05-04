from rest_framework import serializers
from main.models import model_short
class BindSerializer(serializers.ModelSerializer):
    class Meta:
        model = model_short
        fields = '__all__'