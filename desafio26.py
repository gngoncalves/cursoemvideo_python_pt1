frase = str(input('Insira uma frase: ')).strip()
count_a = frase.upper().count('A')
print('Esta frase possui {} vezes a letra "a".'.format(count_a))
find_a = frase.upper().find('A')
print('A letra "a" aparece pela primeira vez na posição {}.'.format(find_a + 1))
find_ra = frase.upper().rfind('A')
print('A letra "a" aparece pela última vez na posição {}.'.format(find_ra + 1))