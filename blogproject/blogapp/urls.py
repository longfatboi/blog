from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('post/<int:postId>', views.getPost),
    path('contact/', views.contact),
    path('commingsoon/', views.CommingSoon),
]