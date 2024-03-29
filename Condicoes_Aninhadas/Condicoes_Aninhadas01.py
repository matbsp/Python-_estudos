from datetime import date
nasc = int(input('Insira seu ano de nascimento: '))
ano_atual = date.today().year
alist = ano_atual - nasc
atraso = alist - 18

if alist < 18 : 
    print ("Fique tranquilo, você ainda não precisa se alistar no exército brasileiro")

elif alist == 18 :
    print ("É necessário o alistamento militar ainda esse ano. ")

else :
    print (f"Seu alistamento militar está {atraso} anos em atraso. ")
