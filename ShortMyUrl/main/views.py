from django.shortcuts import render,redirect
from main.models import model_short
from main.forms import form_long
from main.shortener import shortenerOfUrl
# from rest_framework.response import response
# from rest_framework.redirect import redirect
from django.shortcuts import get_object_or_404
# from rest_framework import generics
# from rest_framework.decorators import api_view
# Create your views here.

def link(request,token):
    url = get_object_or_404(model_short,short_url=token) #[0] the actual object
    return redirect(url.long_url) #redirect to actual url

# class BindAPIView(generics.ListCreateAPIView)
# @api_view(['GET','POST'])
def bind(request):
    form = form_long(request.POST)
    token = ""
    if request.method == 'POST':
        if form.is_valid():
            new_url = form.save(commit=False) #save it
            token = shortenerOfUrl().create_token() #save new token by our shortener.py->create_token
            new_url.short_url = token #save this token to new objects short_url
            new_url.save()
        else:
            form = form_long()
            token = "Invalid URL"
    return render(request,'home.html', { 'form':form,'token':token}) #dictionary for html
