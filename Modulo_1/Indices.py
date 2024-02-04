"""
Exercício
Exiba os indices da lista:

0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria','Helena','Luiz']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])


#Portanto, agora, daria para utilizar isso de forma automática:

lista = ['Maria','Helena','Luiz']
lista.append('João')#tudo o que você atualizar antes do indices, vai ser contado


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])