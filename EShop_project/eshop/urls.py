from django.urls import path
from eshop import views


app_name = 'eshop'

urlpatterns = [
    path('', views.index, name='index'),
]