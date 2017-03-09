from django.shortcuts import render


# Create your views here.
def profile(request, username):
    return render(request, 'user/profile.html', {'username': username})
