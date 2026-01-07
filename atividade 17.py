import math
co= float(input('comprimento do cateto oposto'))
ca= float(input('comprimento do cateto adjacente'))
hi= math.hypot(co,ca)
print('a hipotenusa vai medir  {:.2f}'.format(hi))
#Esse código:
#lê os dois catetos de um triângulo retângulo
#calcula a hipotenusa
#mostra o resultado formatado