from django.db import models

# Create your models here.
class Cliente(models.Model):
 cliente_id = models.AutoField(primary_key=True)
 nombre = models.CharField(max_length=50)
 apellido = models.CharField(max_length=50)
 edad = models.IntegerField(blank=True, null=True)
 email = models.EmailField(unique=True)
 creacion = models.DateTimeField(auto_now_add=True)
 actualizacion = models.DateTimeField(auto_now=True)
 cliente_activo = models.BooleanField(default=True)



"""
CREATE TABLE "cap01_cliente" (
    "cliente_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nombre" varchar(50) NOT NULL,
    "apellido" varchar(50) NOT NULL,
    "edad" integer NOT NULL,
    "email" varchar(254) NOT NULL UNIQUE,
    "creacion" datetime NOT NULL,
    "actualizacion" datetime NOT NULL,
    "cliente_activo" bool NOT NULL
); """