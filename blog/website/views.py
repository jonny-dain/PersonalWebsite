from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{})
def blog(request):
    return render(request, 'blog.html',{})
def blog1(request):
    return render(request, 'blog1.html',{})