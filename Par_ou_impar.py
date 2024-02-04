"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('Digite um número inteiro: ')

try:
    numero = int(numero_str)

    par_ou_impar = (numero % 2 == 0)

    try:
        if par_ou_impar == True:
            print('Seu número é par')

        elif par_ou_impar == False:
            print('Seu número é ímpar')

    except:
        print('Isso não é um número inteiro')

except:
    print('Seu número não é um inteiro!')

