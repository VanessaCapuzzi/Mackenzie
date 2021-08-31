"""Faça um programa em Python que solicite a quantidade de alunos de uma turma.

Após esta informação, o usuário deve digitar a média de cada aluno da turma, e o programa apresentará a mensagem PARABÉNS VOCÊ ESTÁ APROVADO aos alunos com média maior ou igual a 6.0.

O programa deve calcular e mostrar, no final da entrada de dados, a média geral da turma.

Obs.: Caso a quantidade informada de alunos da turma for igual a zero, o programa deve emitir a seguinte mensagem: NÃO HOUVE PROCESSAMENTO
"""

qtdalunos = int(input())
if qtdalunos != 0:
    contador = 0
    notaDeTodos = 0
    while contador < qtdalunos:
        media = float(
            input())
        if(media >= 6.0):
            print("PARABÉNS VOCÊ ESTÁ APROVADO")
        contador += 1
        notaDeTodos += media
    mediaTurma = notaDeTodos/qtdalunos
    print(mediaTurma)
else:
    print("NÃO HOUVE PROCESSAMENTO")

"""
while qtdalunos != 0:
    media = qtdalunos
    media = int(input("digitar a média de cada aluno da turma"))

    if media > 6:
        print("PARABÉNS VOCÊ ESTÁ APROVADO")
    if qtdalunos == 0:
        print("NÃO HOUVE PROCESSAMENTO")
        mediaalunos = media / qtdalunos
"""
