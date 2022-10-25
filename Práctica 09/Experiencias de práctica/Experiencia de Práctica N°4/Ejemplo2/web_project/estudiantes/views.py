from django.shortcuts import render
from django.http import HttpResponse


from. models import Estudiante
# Create your views here.

def index(request):
    estudiantes = Estudiante.objects.all()
    context = {'clase': 'Desarrollo de Aplicaciones', 'estudiantes': estudiantes}
    return render(request,'grupo.html',context)
