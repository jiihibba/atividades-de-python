from random import choice
n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
lista = [n1, n2, n3, n4]
escolhido=choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))
#Esse código:
# recebe o nome de 4 alunos
# guarda os nomes em uma lista
# sorteia um aluno aleatoriamente
# mostra o resultado na tela
