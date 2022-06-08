from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
                raise serializers.ValidationError({'cpf':"digite um cpf valido"})
                #é preciso colocar as chves e especifica o campo que vai receber a validação
        if not nome_valido(data['nome']):
                raise serializers.ValidationError({'nome':"Digite um formato de nome válido"})               
        if not rg_valido(data['rg']):
                raise serializers.ValidationError({'rg':"O rg deve ter 9 dígitos"})
        if not celular_valido(data['celular']):
                raise serializers.ValidationError({'celular':"o celular deve seguir este modelo: 11 91234-1234"})
        return data



    # def validate_nome(self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError(
    #             "Digite um formato de nome válido")
    #     return nome

    # def validate_rg(self, rg):
    #     if len(rg) != 9:
    #         raise serializers.ValidationError("O rg deve ter 9 dígitos")
    #     return rg

    # def validate_celular(self, celular):
    #     if len(celular) < 11:
    #         raise serializers.ValidationError("o celular deve ter 11 dígitos")
    #     return celular
