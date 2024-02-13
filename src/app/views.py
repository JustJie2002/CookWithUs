from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<p1>Welcome To CookWithUs<p1>")