from django.urls import path
from .views import first_web, openTemplate

urlpatterns = [
	path('/', first_web),
	path('/openTemp', openTemplate),
]
