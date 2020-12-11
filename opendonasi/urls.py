from django.urls import path
from . import views

app_name = 'openadopt'

urlpatterns = [
    path('form-request-open-donasi/', views.form_request_open_donasi, name='form_request_open_donasi'),
]
