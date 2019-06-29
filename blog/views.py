from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


def home(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = ContactForm()
	content = {'form': form}
	return render(request, "blog/home.html", content)