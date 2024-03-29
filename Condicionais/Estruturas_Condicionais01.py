valor_casa = float(input( 'Qual o valor da casa? R$'))
salario = float(input('Qual o valor de salario do comprador? R$'))
tempo = float(input('Em quantos meses você pretende pagar esta casa? '))

valor_prestacao = valor_casa/tempo

if valor_prestacao <= salario * 0.30:
    print ('Empréstimo aprovado.')

else:
    print ('Empréstimo negado')
    

    