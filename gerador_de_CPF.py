import random

coletar_valores =''

for i in range(9):
    coletar_valores+=str(random.randint(0,9))

#variaveis
contagem_regressiva = 11
somando_resultados=0
regressiva=12
somar_digitos = 0

#Calculando primeiro digito
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
print(cpf_gerado_calculo)

