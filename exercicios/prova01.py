import random
aluno1 = input("lucas: ")
aluno2 = input("fernando: ")
aluno3 = input("mateus: ")
lista = [aluno1, aluno2, aluno3]
escolhido = random.choice(lista)
print("O aluno escolhido foi: {escolhido}")
