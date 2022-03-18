from django.urls import path
from . import views

urlpatterns = [
    path('', views.SuperList.as_view()),
    path('<int:pk>/', views.SuperDetail.as_view()),
    path('<int:pk>/<int:pk2>/', views.SuperDetail.as_view()),
    path('<str:hero>/<str:villain>/', views.SuperFight.as_view())
]