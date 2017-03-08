from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html', {})


def aboutpage(request):
    return render(request, 'aboutpage.html', {})


def contactpage(request):
    return render(request, 'contactpage.html', {})
	
def index(request):
    return render(request, 'index.html', {})
