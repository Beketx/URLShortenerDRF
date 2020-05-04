from rest_framework import serializers
from main.models import Model_Short
class BindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model_Short
        fields = ['long_url','short_url']