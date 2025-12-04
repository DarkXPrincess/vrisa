from django.shortcuts import render

def index(request):
    return render(request, "index.html")  # suponiendo templates/vrisa/index.html
