# Strings maipulations
print('Strings maipulations')
print()

a = 'casaco'
print(a)

print()

print('Maiúscula')
print(a.upper())

print()

print('Minúscula')
print(a.lower())

print()

print('Capilalize')
print(a.capitalize())

print()

print('Metade ou partes da palavra/string')

print('A partir do caracter 0 até o caracter 3: [cas]aco')
part_of_string = a[0:3]
print(f'Before: {a}')
print(f'After: {part_of_string}')
print()

print('A partir do caracter 3: cas[aco]')
part_of_string = a[3:]
print(f'Before: {a}')
print(f'After: {part_of_string}')

print()

print('Entre os caracteres 2 e 4: ca[sa]co')
part_of_string = a[2:4]
print(f'Before: {a}')
print(f'After: {part_of_string}')

print()

print('Replace texts/strings')
b = a.replace('aco', 'inha')
print('Replace \'aco\' por \'inha\'')
print(f'Before: {a}')
print(f'After: {b}')

print()

print('Replace "o" por "a"')
c = a.replace('o', 'a')
print(f'Before: {a}')
print(f'After: {c}')

print()

print('Finding letter or text or part of some text')
print('find() retorna o "indice" do primeiro elemento econtrado, caso não exista ele retorna -1')
print()
letter_to_find = 's'
letter_marked = "\'" + letter_to_find + "\'"
print(f'Find letter "{letter_to_find}" in {c}')
print(
    f'Na palavra {c.replace(letter_to_find, letter_marked)}, a letra {letter_marked} está na posição de indíce {c.find(letter_to_find)}')

print()
letter_to_find = 'a'
letter_marked = "\'" + letter_to_find + "\'"
print(f'Find letter "{letter_to_find}" in {c}')
print(
    f'Na palavra {c.replace(letter_to_find, letter_marked)}, a letra {letter_marked} está na posição de indíce {c.find(letter_to_find)}')
print(
    f'Note que temos 3 ocorrências da letra {letter_to_find}, porém o método find() retorna apenas o prmeiro que foi encotrado')


print()

print('Tamanho de strings')
e = ' casaco '
marked = "\'" + e + "\'"
print(f'O texto {marked} possui {len(e)} caracteres, contando os espaços no início e no fim do texto')

print()

print(f'Removendo espaços de {marked}')
print(f'Before: {marked}, tamanho: {len(e)}')
f = e.strip()
print(f'After: {f}, tamanho: {len(f)}')

print()

print('Concatenando')
n1 = 14
n2 = 16
print('Primeiro teste')
print('Dividindo {n1} por {n2} o resultado é {n1/n2}')

print('Segundo teste usando f\'\'')
print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')
