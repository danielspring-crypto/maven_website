from django.urls import path
from .import views 

urlpatterns = [
	path('feedback/', views.feedback, name='feedback'),
	path('', views.index, name='index'),
]