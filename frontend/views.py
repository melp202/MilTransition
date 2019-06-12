from django.shortcuts import render

# point react to frontend template
def index(request):
    return render(request, 'frontend/index.html')
