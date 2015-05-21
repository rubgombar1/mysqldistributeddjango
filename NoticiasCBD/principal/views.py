from django.shortcuts import render, redirect
from django.views.generic import CreateView
from principal.forms.AddEditorialForm import AddEditorialForm
from principal.forms.AddNewsForm import AddNewsForm
from principal.forms.AddPersonForm import AddPersonForm
from principal.models import Noticia, Persona, Editorial

# Create your views here.
def news(request):
    news = Noticia.objects.all().order_by('-fecha_pub')
    return render(request, 'news.html', {'news' : news})

def addPerson(request):
    return render(request, "createPerson.html", {'form' : AddPersonForm()})

def savePerson(request):
    if request.method == "POST":
        person = Persona()
        person.nombre = request.POST.get('nombre')
        person.apellidos = request.POST.get('apellidos')
        person.save()
    return redirect('/')

def addEditorial(request):
    return render(request, "createEditorial.html", {'form' : AddEditorialForm()})

def saveEditorial(request):
    if request.method == "POST":
        editorial = Editorial()
        editorial.nombre = request.POST.get('nombre')
        editorial.save()
    return redirect('/')

def addNew(request):
    return render(request, "createEditorial.html", {'form' : AddNewsForm()})

def saveNew(request):
    if request.method == "POST":
        noticia = Noticia()
        noticia.titulo = request.POST.get('titulo')
        noticia.cuerpo = request.POST.get('cuerpo')
        noticia.publicador = Persona.objects.filter(id=request.POST.get('publicadorId'))[0]
        noticia.editoral = Editorial.objects.filter(id=request.POST.get('editorialId'))[0]
        noticia.save()
    return redirect('/')

def detailsNew(request):
    new = Noticia.objects.filter(id=request.GET.get('newId'))[0]
    return render(request, 'detailsNew.html', {'new' : new})