from django.db import models

# Create your models here.

class Administradora(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=140)
    img = models.ImageField("Logo Administradora", upload_to='cotas/static/cotas/images', null=True)
    def __str__(self):
        return str(self.img.url)

class Cota(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=140)
    administradora = models.CharField(max_length=140)
    valor = models.CharField(max_length=140)
    entrada = models.CharField(max_length=140)
    parcelas = models.CharField(max_length=140)
    segmento = models.CharField(max_length=140)
    vencimento = models.CharField(max_length=140)
    img = models.CharField(max_length=255)

    def __str__(self):
        return str(self.codigo)