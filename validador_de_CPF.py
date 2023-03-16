
import re
import sys

#variaveis
entrada=input('Digite seu CPF: ')
cpf= re.sub(r'[^0-9]', '', entrada)
contagem_regressiva = 11
somando_resultados=0
regressiva=12
somar_digitos = 0

#coletando valores do cpf
coletar_valores = cpf[:9]

entrada_sequencia = entrada == entrada[0]* len(entrada)
if entrada_sequencia:
    print('Você enviou dados sequênciais')
    sys.exit()


for valores in coletar_valores:
    contagem_regressiva-=1
    somando_resultados += int(valores)*contagem_regressiva

primeiro_digito = (somando_resultados*10)%11
verificacao_primeiroDigito = primeiro_digito if primeiro_digito <=9 else 0

#calculando segundo digito
coletar_digitos = coletar_valores+str(verificacao_primeiroDigito)

for digitos in coletar_digitos:
    regressiva-=1
    somar_digitos += int(digitos)*regressiva

segundo_digito = (somar_digitos*10)%11
verigicacao_segundoDigio = segundo_digito if segundo_digito<=9 else 0

cpf_gerado_calculo = f'{coletar_valores}{verificacao_primeiroDigito}{verigicacao_segundoDigio}'

if cpf_gerado_calculo == cpf:
    print('CPF Válido')
else:
    print('CPF Invalido')
