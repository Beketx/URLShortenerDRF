from django.shortcuts import redirect
from main.models import Model_Short
from rest_framework.response import Response
from rest_framework.views import APIView
from main.serializers import BindSerializer
from django.shortcuts import get_object_or_404

class LinkAPIView(APIView):
    def get(self,request,token):
        # url = get_object_or_404(Model_Short,short_url=token) #[0] the actual object
        url = Model_Short.objects.filter(short_url=token).first()
        serializer = BindSerializer(url)
        return redirect(url.long_url)



class BindAPIView(APIView):
    def post(self,request):
        serializer = BindSerializer(data=request.data)
        if serializer.is_valid():
            saved_serializer = serializer.save()
        return Response(serializer.data)