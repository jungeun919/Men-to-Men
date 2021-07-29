from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('post/<int:pk>/', views.posting, name="posting"),
    path('post/new_post/', views.new_post, name='new_post'),
    path('post/<int:pk>/remove/', views.remove_post, name='remove_post'),
]