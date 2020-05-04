from django.shortcuts import render,redirect
from main.models import model_short
from main.forms import form_long
from main.shortener import shortenerOfUrl
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from main.serializers import BindSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from django.urls import reverse
# from rest_framework.redirect import redirect
from django.shortcuts import get_object_or_404
# from rest_framework import generics
# from rest_framework.decorators import api_view
# Create your views here.
class LinkAPIView(APIView):
    def get(self,request,token):
        url = get_object_or_404(model_short,short_url=token) #[0] the actual object
        serializer = BindSerializer(url)
        return redirect(url.long_url) #redirect to actual url

class BindAPIView(APIView):
    def get(self,request):
        renderer_classes = [TemplateHTMLRenderer]
        template_name = 'home.html'
        form = form_long()
        return redirect('main/templates/home.html',{'form':form})
    def post(self,request):
        form = request.data
        token = ""
        serializer = BindSerializer(data=form)
        if serializer.is_valid():
            new_url = form.save(commit=False) #save it
            token = shortenerOfUrl().create_token() #save new token by our shortener.py->create_token
            new_url.short_url = token #save this token to new objects short_url
            new_url.save()
            saved_serializer = serializer.save()
        return Response(request,'home.html', { 'form':form,'token':token}) #dictionary for html
