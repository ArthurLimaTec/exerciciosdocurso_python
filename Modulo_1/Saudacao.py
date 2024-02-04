"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Que horas são? ')
horario = int(hora)

if horario >= 18:
    print('Boa Noite!')

elif horario <= 11:
    print('Bom Dia!')

else: 
    print('Boa Tarde!')
