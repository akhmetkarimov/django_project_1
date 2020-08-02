from django.urls import path
from .views import first_web, openTemplate,deleteBlog, changeBlog, BlogViews

urlpatterns = [
	path('/', first_web),
	path('/openTemp', openTemplate),
	path('/openTemp/<int:pk>', deleteBlog),
	path('/openTemp_change', changeBlog),

	path('/blogs', BlogViews.as_view())
]
