from django.urls import path
from main.views import BindAPIView,LinkAPIView
from django.views.generic import TemplateView
urlpatterns = [
    # path('',TemplateView.as_view(template_name='home.html'),name='dom'),
    path('', BindAPIView.as_view(),name='show'),
    path('<str:token>/',LinkAPIView.as_view())
]