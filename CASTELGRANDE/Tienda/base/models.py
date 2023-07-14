from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Clase Tarea con sus aspectos.


class Tarea(models.Model):
    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    
    completos = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.titulo
    
    
    
    #como se va a ordenar la tarea
    #no comprendo aún cómo solucionarlo
    #class Meta:
    #    ordering = ['-completo',]
    