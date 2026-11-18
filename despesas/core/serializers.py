from rest_framework import serializers
from .models import Despesa


class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = [
            "oid_despesa",
            "dat_vencimento_despesa",
            "dat_despesa_pagamento",
            "des_despesa",
            "tpo_despesa",
            "vlr_despesa",
            "vlr_despesa_pago",
            "dat_criacao",
            "dat_alteracao",
        ]