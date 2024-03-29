n0 = float(input('Insira a primeira nota: '))
n1 = float(input('Insira a segunda nota: '))

n2 = n0 + n1
n = n2 / 2

if n < 5.0:
    print ('Reprovado')

elif 5.0 <= n <= 6.9:
    print ('Recuperação')

else:
    print ('Aprovado !!')