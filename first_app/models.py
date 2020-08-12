from django.db import models

class BlogCategory(models.Model):
	category_title = models.CharField(max_length=255)


class Blog(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	categories = models.ManyToManyField(BlogCategory, blank = True, related_name="blogs")
	

