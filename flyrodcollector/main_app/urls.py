from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('flyrods/', views.flyrods_index, name='index_flyrod'),
    path('flyreels/', views.flyreels_index, name='index_flyreel'),
    path('flyrods/<int:flyrod_id>/', views.rod_detail, name='rod_detail'),
    path('flyreels/<int:flyreel_id>/', views.reel_detail, name='reel_detail'),
    path('flyrods/create/', views.RodCreate.as_view(), name='flyrod_create'),
    path('flyrods/<int:pk>/update/', views.RodUpdate.as_view(), name='flyrod_update'),
    path('flyrods/<int:pk>/delete/', views.RodDelete.as_view(), name='flyrod_delete'),
    path('flyreels/create/', views.ReelCreate.as_view(), name='flyreel_create'),
    path('flyreels/<int:pk>/update/', views.ReelUpdate.as_view(), name='flyreel_update'),
    path('flyreels/<int:pk>/delete/', views.ReelDelete.as_view(), name='flyreel_delete'),
    path('flyrods/<int:flyrod_id>/add_trip/', views.add_trip, name='add_trip'),
]