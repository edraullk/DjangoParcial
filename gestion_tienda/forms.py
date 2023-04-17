from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Producto

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nombre de usuario',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingresa tu contraseña',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class RegistrarForm(UserCreationForm):
    class Meta:
      model = User
      fields = ('username','email','password1','password2')
      
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nombre de usuario',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Correo electrónico',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingresa tu contraseña',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repite tu contraseña',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
class NuevoProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre','codigo','image','precioCompra','PrecioVenta','vendido','usuarioReg')
        
        widgets = {
            'usuarioReg':forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'nombre':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'codigo':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'precioCompra':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'PrecioVenta':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        
class EditarProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre','codigo','image','precioCompra','PrecioVenta','vendido','usuarioReg')
        
        widgets = {
            'usuarioReg':forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'nombre':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'codigo':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'precioCompra':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'PrecioVenta':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
   