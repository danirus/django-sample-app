from django.shortcuts import render_to_response

def index(request):
    return render_to_response("index.html")

def home(request):
    return render_to_response("home.html")

def somewhere(request):
    return render_to_response("somewhere.html")
