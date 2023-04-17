from django.contrib.auth.models import User
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    image = models.ImageField(upload_to='producto_imagen', blank=True, null=True)
    precioCompra =models.FloatField()
    PrecioVenta =models.FloatField()
    vendido =models.BooleanField(default=False)
    usuarioReg = models.ForeignKey(User,related_name='productos',on_delete=models.CASCADE)
    
    
    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = 'Productos'
        
    def __str__(self) -> str:
        return self.nombre
