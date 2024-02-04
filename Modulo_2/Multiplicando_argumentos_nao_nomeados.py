# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável

def multi(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

numeros = 2, 5, 10, 20
multiplicação = multi(*numeros)
print(multiplicação)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def par_ou_impar(x):
    resto = x % 2
    
    if resto == 0:
        return print('Par')
    return print('Ímpar')

par_ou_impar(x=305787945689456847)