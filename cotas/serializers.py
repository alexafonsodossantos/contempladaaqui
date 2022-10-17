from rest_framework import serializers
from django.db.models import Avg
from .models import Cota, Parcelas

class ParcelasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parcelas
        fields = [
            'id',
            'qt_parcelas',
            'valor_parcelas'
        ]

class CotaSerializer(serializers.ModelSerializer):
    parcelas = ParcelasSerializer(many=True, read_only=True)
    class Meta:

        model = Cota
        ordering = ['id']
        fields = [
            'id',
            'codigo',
            'administradora',
            'valor',
            'entrada',
            'parcelas',
            'segmento',
            'vencimento',
        ]