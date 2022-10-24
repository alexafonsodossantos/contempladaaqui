from django.db import models

# Create your models here.



class Cota(models.Model):
    id = models.BigAutoField(primary_key=True)
    codigo = models.CharField(max_length=140)
    administradora = models.CharField(max_length=140)
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    entrada = models.DecimalField(max_digits=20, decimal_places=2)
    segmento = models.CharField(max_length=140)
    vencimento = models.IntegerField()

    def __str__(self):
        return str(self.codigo)

class Parcelas(models.Model):
    id = models.BigAutoField(primary_key=True)
    cota_id = models.ForeignKey(Cota, related_name='parcelas', on_delete=models.CASCADE)
    qt_parcelas = models.IntegerField()
    valor_parcelas = models.DecimalField(decimal_places=2, max_digits=10)


class Imagem(models.Model):
    cota_cod = models.ForeignKey(Cota, on_delete=models.CASCADE)
    img = models.ImageField("Arte", upload_to='cotas/static/images', null=True)

