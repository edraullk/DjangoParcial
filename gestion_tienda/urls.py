from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'gestion_tienda'
urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('registrar/', views.registrar, name='registrar'),
    path('nuevo/', views.new, name='nuevo'),
    path('<int:pk>/', views.detail, name='detail' ),
    path('<int:pk>/eliminar', views.eliminar, name='eliminar' ),
    path('<int:pk>/editar', views.editar, name='editar' ),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name='login'),
]