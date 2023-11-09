from django.shortcuts import render
from .models import Destination
from .models import Teams

# Create your views here.
def demoFunction(request):
    obj = Destination.objects.all()
    teams = Teams.objects.all()
    return render(request, "index.html", {'results':obj, 'members':teams})
