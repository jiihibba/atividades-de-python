import random
n1=int(input('primeiro aluno'))
n2=int(input('segundo aluno'))
n3=int(input('terceiro aluno'))
n4=int(input('terceiro aluno'))
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print('a ordem de apresetação será')
print(lista)
#Esse código:
# lê 4 valores
# guarda em uma lista
# embaralha a ordem
# mostra a nova ordem