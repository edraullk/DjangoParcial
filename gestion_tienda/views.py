from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Producto

from .forms import RegistrarForm, NuevoProducto,EditarProducto


# Create your views here.
@login_required
def index(request):
    productos = Producto.objects.filter(vendido=False)[0:6]
    return render(request, 'index.html',{
        'productos':productos,
    })

def contacto(request):
    return render(request,'contacto.html')

def registrar(request):
    if request.method =='POST':
        form = RegistrarForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = RegistrarForm()
    
    return render(request, 'registrar.html',{
        'form':form
    })
    
def detail(request,pk):
    producto = get_object_or_404(Producto,pk=pk)
    
    return render(request,'detail.html',{
        'producto': producto
    })

@login_required  
def new(request):
    if request.method == 'POST':
        form = NuevoProducto(request.POST, request.FILES)
        
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuarioReg = request.user
            producto.save()

            return redirect('gestion_tienda:detail', pk=producto.id)
    else:
        form=NuevoProducto()
    
    return render(request, 'form.html',{
        'form': form,
        'title': 'Nuevo Producto',
    })
    
@login_required
def eliminar(request, pk):
    producto = get_object_or_404(Producto,pk=pk, usuarioReg=request.user)
    producto.delete()

    return redirect('gestion_tienda:index')


@login_required  
def editar(request, pk):
    producto = get_object_or_404(Producto,pk=pk, usuarioReg=request.user)
    if request.method == 'POST':
        form = EditarProducto(request.POST, request.FILES, instance=producto)
        
        if form.is_valid():
            form.save()
            
            return redirect('gestion_tienda:detail', pk=producto.id)
    else:
        form=EditarProducto(instance=producto)
    
    return render(request, 'form.html',{
        'form': form,
        'title': 'Editar Producto',
    })
    