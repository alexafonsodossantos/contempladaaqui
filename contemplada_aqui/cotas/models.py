from django.db import models

# Create your models here.

class Administradora:
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=140)
    img = odels.ImageField("Logo Administradora", upload_to='cotas/static/cotas/images', null=True)
    def __str__(self):
        return str(self.img.url)

class Cota(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=140)
    administradora = models.CharField(max_length=140)
    valor = models.FloatField()
    entrada = models.FloatField()
    parcelas = models.IntegerField()
    segmento = models.ImageField("Product Image", upload_to='loja/static/loja/images', null=True)
    vencimento = models.TextField()
    img = models.ForeignKey(Administradora, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codigo)