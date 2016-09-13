from django.shortcuts import render, render_to_response
from sati import session
# from django.http import HttpResponse


# def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    print "index"
    return render(request, 'public/index.html')


def login(request):
    print "login"
    if request.session.get('has_logged'):
        return render(request, 'dashboard/index.html')
    else:
        return render(request, 'public/login.html')


def signup(request):
    return render(request, 'public/signup.html')


def new_login(request):
    return render(request, 'public/login.html')

# Events


def event(request):
    return render(request, 'event/index.html')

