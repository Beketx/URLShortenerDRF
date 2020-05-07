from django.urls import path
from main.views import BindAPIView,LinkAPIView

urlpatterns = [
    path('', BindAPIView.as_view()),
    path('<str:token>/',LinkAPIView.as_view())
]