from django.urls import path
from .views import index, detail_filmu

urlpatterns = [
    path('', index),
    path('<slug:film>/', detail_filmu),
]