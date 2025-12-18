dias=input('quantos dias alugados')
km=float(input('quantos km rodados'))
pago=(dias*60)+(km*0.15)
print('o total a pagar e de R${:.2f}'.format(pago))