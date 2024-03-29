from datetime import date
num = int(input('Digite um ano qualquer, DIGITE 0 PARA O ANO ATUAL '))
if num == 0:
    num = date.today().year

if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print (f'\33[4;34m{num}\33[m é um ano BISSEXTO. ')
else:
    print (f'\33[0;34;40m{num}\33[m não é um ano \33[1;34;40mBISSEXTO.\033[m')