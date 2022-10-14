from rest_framework import serializers
from django.db.models import Avg
from .models import Cota

class CotaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cota
        fields = (
            'codigo',
            'administradora',
            'valor',
            'entrada',
            'parcelas',
            'segmento',
            'vencimento',
            'img'
        )