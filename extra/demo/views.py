from django.shortcuts import render_to_response as render

def index(request):
    return render("index.html")
