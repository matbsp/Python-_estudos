frase = input('Escreva uma frase qualquer: ')
letra = input('Escreva qual letra você quer contar na frase: ')
fras = frase.lower().count(letra)

print (f'A letra (a) aparece {fras} vezes na frase `{frase}')
