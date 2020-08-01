from django import forms


class BlogForm(forms.Form):
	title = forms.CharField(max_length=255)
	description = forms.CharField(max_length=500)