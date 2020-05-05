from rest_framework import serializers
from main.models import Model_Short
from main.shortener import ShortenerOfUrl
class BindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model_Short
        fields = ['long_url','short_url']
#
# class BindSerializer(serializers.Serializer):
#     long_url = serializers.URLField()
#     short_url = serializers.CharField(max_length=20)
#     token = ShortenerOfUrl().create_token()
#     def create(self, validated_data):
#         new_url = Model_Short.objects.create(long_url = validated_data['long_url'],short_url = self.token)
#         return new_url
