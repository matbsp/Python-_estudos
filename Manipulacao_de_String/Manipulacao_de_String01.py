num = input('Digite um número de 0 a 9999 para verificarmos: ')

num = num.zfill(4)

print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))