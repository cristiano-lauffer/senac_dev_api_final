from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Despesa
from .serializers import DespesaSerializer


class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

    @action(detail=False, methods=['get'], url_path='tipo/(?P<tipo>[^/.]+)')
    def por_tipo(self, request, tipo=None):
        despesas = self.queryset.filter(tpo_despesa__icontains=tipo)
        serializer = self.get_serializer(despesas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='descricao/(?P<descricao>[^/.]+)')
    def por_descricao(self, request, descricao=None):
        despesas = self.queryset.filter(des_despesa__icontains=descricao)
        serializer = self.get_serializer(despesas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='vencimento/(?P<data>[0-9]{4}-[0-9]{2}-[0-9]{2})')
    def por_vencimento(self, request, data=None):
        despesas = self.queryset.filter(dat_vencimento_despesa=data)
        serializer = self.get_serializer(despesas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='pagamento/(?P<data>[0-9]{4}-[0-9]{2}-[0-9]{2})')
    def por_pagamento(self, request, data=None):
        despesas = self.queryset.filter(dat_despesa_pagamento=data)
        serializer = self.get_serializer(despesas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='nao-pagas')
    def nao_pagas(self, request):
        despesas = self.queryset.filter(dat_despesa_pagamento__isnull=True)
        serializer = self.get_serializer(despesas, many=True)
        return Response(serializer.data)