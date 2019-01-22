from django.urls import path
from . import views

app_name = 'history'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # localhost:8000/1/
    path('<int:artist_id>/', views.detail, name='detail'),
]