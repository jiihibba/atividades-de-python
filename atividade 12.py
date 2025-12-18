p=float(input("qual o preço do produto com desconto de 5%?: "))
np=p-(p*5/100)
print('produto que custava R${:.2f},na promoção com o desconto de 5% vai custar R${:.2f}'.format(p,np))