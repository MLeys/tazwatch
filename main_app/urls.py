from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('tazs/', views.tazs_index, name="index"),
    path('tazs/<int:taz_id>/', views.tazs_detail, name="detail"),
    path('tazs/create/', views.TazCreate.as_view(), name='tazs_create'),
]
