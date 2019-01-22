from django.urls import path
from . import views

app_name = 'history'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    
]