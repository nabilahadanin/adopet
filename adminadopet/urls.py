from django.urls import path
from . import views

app_name = 'adminadopet'

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('eval-open-donasi/', views.eval_open_donasi, name='eval_open_donasi'),
]
