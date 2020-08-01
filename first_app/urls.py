from django.urls import path
from .views import first_web, openTemplate, deleteBlog

urlpatterns = [
	path('/', first_web),
	path('/openTemp', openTemplate),
	path('/openTemp/<int:pk>', deleteBlog),
]
