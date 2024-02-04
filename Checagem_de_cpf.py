"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
  ----------------------------
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

#PREPARANDO O CPF PARA OS CÁLCULOS:
entrada = '709.626.310-19'
copia = entrada
caracteres_indesejados = ['.', '-']

#retirando os pontos e traços:
for caractere in caracteres_indesejados:
    entrada = entrada.replace(caractere, '')

cpf = [int(digito) for digito in str(entrada)] #transformando str em lista int e deletando os dois últimos dígitos para calculá-los
del cpf[-1]
del cpf[-1]

#preparando os recursos da regra de cálculo:
lista_regressiva = [10,9,8,7,6,5,4,3,2]
#CALCULANDO:
step = 1

while step <= 2:
    i = 0
    multiplicacao = []
    lr = len(lista_regressiva)

    while i < lr:
        
        multiplicacao.append(cpf[i] * lista_regressiva[i])
        i += 1
        
    soma_e_mult = sum(multiplicacao) * 10
    resto = soma_e_mult%11
    lista_regressiva.insert(0,11)
    
    if resto > 9:
        cpf.append(0)

    else:
        cpf.append(resto)
    
    print(cpf)
    step += 1


#Trás o resultado em lista str para comparar com a entrada: 
cpf_str = list(map(str, cpf))
if cpf_str == list(entrada):
    print('Validação aceita!')

else:
    print('Validação recusada!')
