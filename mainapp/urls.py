
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('view_report/<str:pk>/', views.viewReport, name='view_report'),
    path('add/', views.addPhoto, name='add'),
    

    path('report/', views.report, name='report'),
    path('members/', views.members, name='members'),
    path('about/', views.about, name='about'),

    path('login/', views.login, name='login'),
    path('login/', views.login, name='admin_login'),
    path('logout/', views.logout, name='logout'),
    path('admin_user/', views.admin_user, name='admin_user'),

    path('test/', views.test, name='test'),


]