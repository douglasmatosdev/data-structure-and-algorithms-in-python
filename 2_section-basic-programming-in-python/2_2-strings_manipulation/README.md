# Strings maipulations

```python
a = 'casaco'
print(a) # casaco
```

### Maiúscula

```python
a = 'casaco'
print(a.upper()) #CASACO
```

### Minúscula

```python
a = 'casaco'
print(a.lower()) # casaco
```

### Capilalize

```python
a = 'casaco'
print(a.capitalize()) # Casaco
```

### Metade ou partes da palavra/string

```python
a = 'casaco'
print('A partir do caracter 0 até o caracter 3: [cas]aco')
part_of_string = a[0:3]

print(f'Before: {a}') #casaco
print(f'After: {part_of_string}') # cas
```

### A partir do caracter 3: cas[aco]

```python
a = 'casaco'
part_of_string = a[3:]

print(f'Before: {a}') # casaco
print(f'After: {part_of_string}') # aco
```

### Entre os caracteres 2 e 4: ca[sa]co

```python
a = 'casaco'
part_of_string = a[2:4]

print(f'Before: {a}') # casaco
print(f'After: {part_of_string}') # sa
```

### Replace texts/strings

> Replace \'aco\' por \'inha\'

```python
a = 'casaco'
b = a.replace('aco', 'inha')

print(f'Before: {a}') # casaco
print(f'After: {b}') # casinha
```

### Replace "o" por "a"

```python
a = 'casaco'
c = a.replace('o', 'a')

print(f'Before: {a}') # casaco
print(f'After: {c}') # casaca
```

### Finding letter or text or part of some text

> find() retorna o "indice" do primeiro elemento econtrado, caso não exista ele retorna -1

```python
a = 'casaco'
c = a.replace('o', 'a')
letter_to_find = 's'
letter_marked = "\'" + letter_to_find + "\'"
print(f'Find letter "{letter_to_find}" in {c}') # Find letter "s" in casaca
print(
    f'Na palavra {c.replace(letter_to_find, letter_marked)}, a letra {letter_marked} está na posição de indíce {c.find(letter_to_find)}') # Na palavra ca's'aca, a letra 's' está na posição de indíce 2
```

```python
a = 'casaco'
c = a.replace('o', 'a')
letter_to_find = 'a'
letter_marked = "\'" + letter_to_find + "\'"
print(f'Find letter "{letter_to_find}" in {c}') # Find letter "a" in casaca
print(
    f'Na palavra {c.replace(letter_to_find, letter_marked)}, a letra {letter_marked} está na posição de indíce {c.find(letter_to_find)}') # Na palavra c'a's'a'c'a', a letra 'a' está na posição de indíce 1
```

> Note que temos 3 ocorrências da letra 'a', porém o método find() retorna apenas o prmeiro que foi encotrado

### Tamanho de strings

```python
e = ' casaco '
marked = "\'" + e + "\'"
print(f'O texto {marked} possui {len(e)} caracteres, contando os espaços no início e no fim do texto')
```

### Removendo espaços de '&nbsp;&nbsp;casaco&nbsp;&nbsp;'

```python
print(f'Before: {marked}, tamanho: {len(e)}') # Before: ' casaco ', tamanho: 8
f = e.strip()
print(f'After: {f}, tamanho: {len(f)}') # After: casaco, tamanho: 6
```

### Concatenando

#### Primeiro teste

```python
n1 = 14
n2 = 16
print('Dividindo {n1} por {n2} o resultado é {n1/n2}') # Dividindo {n1} por {n2} o resultado é {n1/n2}
```

#### Segundo teste usando f''

```python
print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}') # Dividindo 14 por 16 o resultado é 0.875
```
