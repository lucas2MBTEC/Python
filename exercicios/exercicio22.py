from random import shuffle
aluno01 = str(input('primeiro aluno:'))
aluno02 = str(input('o segundo aluno:'))
aluno03 = str(input('o terceiro aluno:'))
aluno04 = str(input('o quarto aluno:'))
lista = [aluno01, aluno02, aluno03, aluno04]
shuffle(lista)
print('a ordem da apresentação será{}'.format(lista))
