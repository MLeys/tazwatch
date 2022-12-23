from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('tazs/', views.tazs_index, name="index"),
    path('tazs/<int:taz_id>/', views.tazs_detail, name="detail"),
    path('tazs/create/', views.TazCreate.as_view(), name='tazs_create'),
    path('tazs/<int:pk>/update/', views.TazUpdate.as_view(), name='tazs_update'),
    path('tazs/<int:pk>/delete/', views.TazDelete.as_view(), name='tazs_delete'),
]
