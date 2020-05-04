from rest_framework import serialziers
from main.models import model_short
class BindSerializer(serialziers.ModelSerializer):
    class Meta:
        model = model_short
        fields = '__all__'