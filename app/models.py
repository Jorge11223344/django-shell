from django.db import models

# Create your models here.
class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True, default="mail@mail.com")
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


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()


class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True) #cada emtrada queda con fecha del servidor , al instanciar una entrada se genera la fecha actual
    autor = models.ForeignKey(Autor,  on_delete=models.CASCADE, null=True, blank=True) #al principio dejarlo siempre con nul y blank, y al pasarlo a produccion lo sacamos


class ClienteTest(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(null=True,blank=True)
    creacion =models.DateTimeField(auto_now_add=True)
    actualización =models.DateTimeField(auto_now=True)

class Direccion(models.Model):
    cliente = models.OneToOneField(ClienteTest, blank=False, null=False, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100, blank=False, null=False)
    numero = models.CharField(max_length=10, blank=False, null=False)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=100, blank=False, null=False)
    ciudad = models.CharField(max_length=100, blank=False, null=False)


