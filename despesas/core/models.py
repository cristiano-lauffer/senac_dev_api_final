from django.db import models

class Despesa(models.Model):
    oid_despesa = models.BigAutoField(primary_key=True)
    dat_vencimento_despesa = models.DateField()
    dat_despesa_pagamento = models.DateField(null=True, blank=True)

    des_despesa = models.CharField(max_length=500)
    tpo_despesa = models.CharField(max_length=500)

    vlr_despesa = models.DecimalField(max_digits=12, decimal_places=2)
    vlr_despesa_pago = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    dat_criacao = models.DateTimeField(auto_now_add=True)
    dat_alteracao = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "despesas"

    def __str__(self):
        return self.des_despesa
