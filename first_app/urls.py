from django.urls import path
# from .views import first_web, openTemplate,deleteBlog, changeBlog, BlogViews
from .views import BlogViews, BlogDetailViews, BlogCategoryViews, BlogCategoryDetailViews

urlpatterns = [
	# path('/', first_web),
	# path('/openTemp', openTemplate),
	# path('/openTemp/<int:pk>', deleteBlog),
	# path('/openTemp_change', changeBlog),

	path('blogs', BlogViews.as_view()),
	path('blogs/<int:pk>', BlogDetailViews.as_view()),

	path('blog_categories', BlogCategoryViews.as_view()),
	path('blog_categories/<int:pk>', BlogCategoryDetailViews.as_view()),
]
