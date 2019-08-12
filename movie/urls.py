from django.urls import path
from . import views
urlpatterns = [
	path('', views.movie_show, name = 'movie_show'),
	path('<int:pk>/', views.movie_detail, name = 'movie_detail'),
]