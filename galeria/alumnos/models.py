from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.

class TiposObras(models.Model):
    id_tipo          = models.AutoField(db_column='id_tipo', primary_key=True) 
    descripcion     = models.CharField(max_length=150 )

    def __str__(self):
        return str(self.descripcion)





class Obras(models.Model):
    codigo           = models.CharField(primary_key=True, max_length=6, verbose_name='codigo')
    nombre          = models.CharField(max_length=150, verbose_name='nombre')
    nombre_autor           = models.CharField(max_length=150, verbose_name='nombre_autor')
    tipo          =models.IntegerField(verbose_name='tipo')
    estado           = models.IntegerField(verbose_name='estado')
    descripcion          = models.TextField(verbose_name='descripcion')
    img              = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='img')
    
    class Meta:      
        ordering = ['nombre']

    def delete(self, using=None, keep_parents=False):
        self.img.storage.delete(self.img.name)
        return super().delete()
