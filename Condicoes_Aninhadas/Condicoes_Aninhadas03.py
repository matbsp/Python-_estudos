num = int(input('Escrevas um número inteiro qualquer: '))
conversao = int(input('Digite um número para definir a base de conversão \n 1 - HEXADECIMAL, \n 2 - BINÁRIO \n 3 - OCTADECIMAL \n '))
binario = bin (num)
hexadecimal = hex(num)
octal = oct(num)

if conversao == 1:
    print (f'{hexadecimal}')

elif conversao == 2:
    print (f'{binario}')

elif conversao == 3:
    print (f'octal')

else:
    print ('Por favor insira um número de 1 a 3 para a conversão' )