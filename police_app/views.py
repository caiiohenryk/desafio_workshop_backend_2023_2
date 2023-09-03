from django.shortcuts import render
from rest_framework import generics
from .models import Pessoa, Ocorrencia
from .serializer import PessoaSerializer, OcorrenciaSerializer

# Criando a ficha de Pessoa e Ocorrencias
class PessoaListCreate(generics.ListCreateAPIView):
    
    serializer_class = PessoaSerializer

# Query
    def get_queryset(self):
        queryset = Pessoa.objects.all()
        ocorrencia = self.request.query_params.get('ocorrencia')
        if ocorrencia is not None:
            queryset = queryset.filter(pessoa=ocorrencia)
        return queryset

class OcorrenciaListCreate(generics.ListCreateAPIView):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer


# para puxar, atualizar ou deletar uma ficha:

class PessoaRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class OcorrenciaRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ocorrencia.objects.all()
    serializer_class = OcorrenciaSerializer