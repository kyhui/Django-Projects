from django.shortcuts import render
from .forms import AddManga, ContactForm

def home(request):
	context = {}
	return render(request, "home.html",context)

def contact(request):
	form = ContactForm(request.POST or None)

	context = {
		"form": form,
	}
	return render(request, "form.html", context)

def addChapters(request):
	title = "My Title %s " %(request.user)
	form = AddManga(request.POST)

	if form.is_valid():
		instance = form.save(commit=False)

	context = {
		"template_title": title,
		"form": form,
	}
	return render(request, "addChapters.html", context)

