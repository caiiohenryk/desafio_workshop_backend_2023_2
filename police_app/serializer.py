from rest_framework import serializers
from .models import Pessoa, Ocorrencia


# Criando os serializers das classes em models, para conseguir visualizar os dados na web.

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'cpf')

class OcorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocorrencia
        fields = ('id', 'tipodeocorrencia', 'pessoa', 'oc_date', 'descricaoOcorrencia')