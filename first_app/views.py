from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.http import HttpResponse
from .forms import BlogForm

from .models import Blog


from rest_framework.views import APIView
from rest_framework.response import Response
from .seralizations import BlogSerializer
from rest_framework import status

# Django Rest Framework


class BlogViews(APIView):
	serializers_class = BlogSerializer

	def get(self, request):
		blogs = Blog.objects.all()
		serializer = self.serializers_class(blogs, many=True)
		return Response(serializer.data)

	
	def post(self, request):
		serializer = self.serializers_class(data=request.data)
		
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
			
		else:
			return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

























# Create your views here.

def first_web(request):

	# Create node
	# INSERT INTO 
	# Blog.objects.create(title="New Title from Viwes", description="New Description from Views")
	
	# Get All nodes
	# SELECT
	# Blog.objects.all()/Blog.objects.all().values()

	# Get by where
	# SELECT * FROM Blog WHERE title = ""
	# Blog.objects.all().filter(title="New Title from Viwes").values()
	
	# Get by where
	# SELECT * FROM Blog WHERE id = 2
	# Blog.objects.get(pk=1)

	return HttpResponse(Blog.objects.get(title="New Title from Viwes"))


def openTemplate(request):
	header = "My Header"
	myform = BlogForm()
	# data = {"header": header}

	if request.method == "POST":
		title = request.POST.get("title")
		description = request.POST.get("description")
		Blog.objects.create(title=title, description=description)	


	myvar = {
			"my_data": "new my data",
			"my_list": [1,2,3,4,5],
			"form": myform,
			"blogs":Blog.objects.all()
		}
	return render(request, 'test.html', myvar)

	# return TemplateResponse(request, 'test.html')


# CRUD
# Create, Read, Update, Delete

def changeBlog(request):
	title = request.POST.get("title")
	description = request.POST.get("description")
	pk = request.POST.get("pk")
	Blog.objects.filter(pk=pk).update(title=title, description=description)
	return redirect('/first_app/openTemp')


def deleteBlog(request, pk):
	Blog.objects.get(pk=pk).delete()
	return redirect('/first_app/openTemp')



"""



Back-end:

	1) Django
	2) Node.js
	3) PHP

Front-end:

	1) React
	2) Angular

HTML, CSS, JS, JQuery(Ajax)

DevOps: 

	1) Git

SQL:

	1) MySQL
	2) PostgreSQL
	3) NoSQL - MongoDB



"""


















