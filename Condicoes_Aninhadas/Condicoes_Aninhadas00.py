n1 = float (input ('Insira a primeira nota: '))
n2 = float (input ('Insira a segunda nota: '))

n3 = n1 + n2
n = n3 / 2

if n < 5.0:
    print ('Reprovado')

elif 5.0 <= n <= 6.9:
    print ('Recuperação')

else :
    print ('Aprovado !! ')
    