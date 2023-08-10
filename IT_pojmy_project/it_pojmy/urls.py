from django.urls import path
from it_pojmy import views

app_name = 'it_pojmy'

urlpatterns = [
    path('', views.home, name='home'),
    path('seznam/', views.seznam, name='seznam'),

    # /detail/hardware/
    # /detail/software/
    # /detail/python/
    path('detail/<slug:zkratka>/', views.detail, name='detail'),
    path('novy-komentar/', views.novy_komentar, name='novy_komentar'),
    path('novy-clanek/', views.ClanekCreateView.as_view(), name='ClanekCreateView'),

    path('clanky/', views.seznam_clanku, name='seznam_clanku'),
    path('clanky2/', views.ClanekList.as_view(), name='ClanekList'),
    path('clanky/<slug:slug_url>/', views.detail_clanku, name='detail_clanku'),
]