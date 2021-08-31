#Faça um programa em Python que, dada a idade de um atleta que será digitada pelo usuário, apresente a mensagem da coluna CATEGORIA de acordo com a tabela abaixo, onde a categoria depende da idade de entrada. 

n1 = int(input())

if n1 < 5:
    print('NÃO TEM IDADE PARA SER ATLETA')
elif n1 >= 5 and n1 <= 7:
    print('INFANTIL A')
elif n1 >= 8 and n1 <= 10:
    print('INFANTIL B')
elif n1 >= 11 and n1 <= 13:
    print('JUVENIL A')
elif n1 >= 14 and n1 <= 17:
    print('JUVENIL B')
else:
    print('SÊNIOR')
