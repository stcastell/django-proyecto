from django.db import models

class Articulo(models.Model):
	nombre = models.CharField(max_length=255, default='',null=False)
	descripcion = models.CharField(max_length=300, default='',null=False)
	precio = models.IntegerField(default=0,null=False)
	ruta = models.CharField(max_length=255, default='',null=False)

