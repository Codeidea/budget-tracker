from django.shortcuts import render

def homepage(request):
    return render(request, 'frontend/index.html', {})

def app(request):
    return render(request, 'frontend/app.html', {})