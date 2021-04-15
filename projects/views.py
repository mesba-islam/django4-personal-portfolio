from django.shortcuts import render
from.models import Project

def home(request):
    pro= Project.objects.all()
    return render(request, 'projects/home.html', {'projects':pro})
    
def about(request):
    return render(request,'projects/about.html')


def contact(request):
    return render(request,'projects/contact.html')