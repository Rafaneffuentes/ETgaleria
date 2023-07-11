
from django.shortcuts import render, redirect
from .models import  TiposObras, Obras
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, User

from .forms import ObrasForm

# Create your views here.

#def base(request):
#    return render(request, 'alumnos/base.html')

def home(request):
    return render(request, 'alumnos/home.html')
def nosotros(request):
    return render(request, 'alumnos/nosotros.html')
def contacto(request):
    return render(request, 'alumnos/contacto.html')
def obras(request):
    obras = Obras.objects.all()
    for obr in obras:
        if obr.estado == 1:
            obr.estado = 'En exposición'
        else:
            obr.estado = 'En bodega'
        
        if obr.tipo == 1:
            obr.tipo = 'Orfebrería'
        elif obr.tipo == 2:
            obr.tipo = 'Pintura'
        else:
            obr.tipo = 'Escultura'
    context={"obras":obras}
    return render(request, 'alumnos/obras.html', context)


## GESTION DE CURSOS
@login_required
def gestioncur(request):
    obras = Obras.objects.all()
    for obr in obras:
        if obr.estado == 1:
            obr.estado = 'En exposición'
        else:
            obr.estado = 'En bodega'

        if obr.tipo == 1:
            obr.tipo = 'Orfebrería'
        elif obr.tipo == 2:
            obr.tipo = 'Pintura'
        else:
            obr.tipo = 'Escultura'

    context={"obras":obras}
    return render(request, 'alumnos/gestion/gestioncur.html', context)


# CRUD
# https://www.youtube.com/watch?v=ezIj71CX944
@login_required
@permission_required('alumnos.add_obras')
def nuevocur(request):
    formulario = ObrasForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
       formulario.save()
       return redirect('gestioncur')
    return render(request, "alumnos/gestion/nuevocurso.html", {"formulario": formulario})

@login_required
@permission_required('alumnos.change_obras')
def editarcur(request, codigo):
    obras = Obras.objects.get(codigo=codigo)
    formulario = ObrasForm(request.POST or None, request.FILES or None, instance=obras)
    if formulario.is_valid() and request.POST:
       formulario.save()
       return redirect('gestioncur')
    return render(request, "alumnos/gestion/editarcurso.html", {"formulario": formulario})

@login_required
@permission_required('alumnos.delete_obras')
def borrarcurso(request, codigo):
    obras = Obras.objects.get(codigo=codigo)
    obras.delete()
    messages.success(request, 'Obra Eliminada!')
    return redirect('gestioncur')


def verobra(request, codigo):
    obras = Obras.objects.filter(codigo=codigo)
    for obr in obras:
        if obr.estado == 1:
            obr.estado = 'En exposición'
        else:
            obr.estado = 'En bodega'

        if obr.tipo == 1:
            obr.tipo = 'Orfebrería'
        elif obr.tipo == 2:
            obr.tipo = 'Pintura'
        else:
            obr.tipo = 'Escultura'

    context={"obras":obras}
    return render(request, 'alumnos/gestion/verobra.html', context)
