
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('project', views.ProjcetView.as_view()),
    # path('project/<int:pk>/', views.ProjcetView.as_view()),
]