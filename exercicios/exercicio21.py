from random import choice
aluno01 = str (input('pirimeiro aluno :'))
aluno02 = str (input('segundo aluno :'))
aluno03 = str (input('terceiro aluno :'))
aluno04 = str (input('quarto aluno :'))
lista = [aluno01, aluno02, aluno03, aluno04]
escolhido = choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))
