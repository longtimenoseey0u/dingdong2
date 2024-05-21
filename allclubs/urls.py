from django.urls import path
from .views import look

app_name = 'allclubs'

urlpatterns = [
    path('', look, name='look'),
]