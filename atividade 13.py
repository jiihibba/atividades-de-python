salario=float(input('qual salario do funcionario? R$'))
novo=salario+(salario*33/100)
print('um funcionario que ganhava R${:.2f},com o aumento,passa a R${:.2f}'.format(salario,novo))