from django.urls import path
from main.views import bind,link
urlpatterns = [
    path('', bind),
    path('<str:token>',link)
]