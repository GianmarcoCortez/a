from django.db import models

# Create your models here.
class EmpresaPequeña(models.Model):
    nombre=models.CharField(max_length=30)
    documentos=models.PositiveSmallIntegerField()