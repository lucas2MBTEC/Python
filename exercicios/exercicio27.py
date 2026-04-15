# Script para demonstrar remoção de espaços em branco de uma string
# 1. Remove espaços do início e final (strip())
# 2. Remove apenas da esquerda (lstrip())
# 3. Remove apenas da direita (rstrip())

texto = input('Digite uma string com espaços: ')

print('Original:', repr(texto))  # repr mostra espaços claramente

sem_espacos = texto.strip()
print('Sem espaços início e fim (strip()):', repr(sem_espacos))

sem_esquerda = texto.lstrip()
print('Sem espaço à esquerda (lstrip()):', repr(sem_esquerda))

sem_direita = texto.rstrip()
print('Sem espaço à direita (rstrip()):', repr(sem_direita))
