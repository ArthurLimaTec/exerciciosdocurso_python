"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir,
    apagar ou listar
Não permita que o programa quebre com erros
    de indices inexistentes na lista
"""
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

lista = []

while True:

    entrada = input("Selecione uma opção:\n[i]nserir [a]pagar [l]istar: ")

    if entrada == "i":
        a = input("Valor: ")
        lista.append(a)
        continue
        
    elif entrada == "a":
        b = input("Escolha o índice para apagar: ")
        
        try:
            c = int(b)
            del lista[c]
        except IndexError:
            print('Índice inexistente!')
        except ValueError:
            print('Por favor, digite um número inteiro.')
        
    elif entrada == "l":
        for indice,nome in enumerate(lista):
            print(indice,nome)
        continue

