from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import documento
from .forms import documentoform
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def documentos(request):
    documentos = documento.objects.all()
    return render(request, 'documentos/index.html',{'documentos':documentos})

def crear(request):
    formulario = documentoform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('documentos')
    return render(request, 'documentos/crear.html',{'formulario':formulario})

def editar(request,id):
    documentacion = documento.objects.get(id=id)
    formulario = documentoform(request.POST or None, request.FILES or None, instance=documentacion)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('documentos')
    return render(request, 'documentos/editar.html', {'formulario':formulario})

def ver(request,id):
    archivo = documento.objects.get(id=id)
    print(archivo)
   # formulario = documentoform(request.POST or None, request.FILES or None, instance=archivo)
    
    return render(request, 'documentos/ver.html', {'formulario':archivo})

def eliminar(request,id):
    document = documento.objects.get(id=id)
    # print(document)
    document.delete()
    return redirect('documentos')