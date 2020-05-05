from django.shortcuts import render,redirect
from main.models import Model_Short
from main.shortener import ShortenerOfUrl
from rest_framework.response import Response
from rest_framework.views import APIView
from main.serializers import BindSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

class LinkAPIView(APIView):
    token = ShortenerOfUrl().create_token()  # save new token by our shortener.py->create_token

    def get(self,request,token):
        url = get_object_or_404(Model_Short,short_url=token) #[0] the actual object
        # url = Model_Short.objects.filter(short_url=token).first()
        serializer = BindSerializer(url)
        # return Response(serializer.data) #redirect to actual url
        # return redirect(serializer.data)
        return redirect(request.query_params['long_url'])
        # return HttpResponseRedirect(serializer.data)


class BindAPIView(APIView):
    token = ShortenerOfUrl().create_token()  # save new token by our shortener.py->create_token
    def post(self,request):
        form = request.data
        new_url = Model_Short.objects.create(long_url=form,short_url=self.token)
        serializer = BindSerializer(data=new_url)
        if serializer.is_valid():
            saved_serializer = serializer.save()
        return Response(serializer.data)