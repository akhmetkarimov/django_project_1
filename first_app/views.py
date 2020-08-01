from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.http import HttpResponse
from .forms import BlogForm

from .models import Blog

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


















