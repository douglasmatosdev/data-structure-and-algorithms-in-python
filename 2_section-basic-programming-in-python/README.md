# Manipulation of variables and constants

### Variáveis e constantes

- Por meio de variáveis que um algortimo “guarda” os dados do problema

- Todo dado que tem a possibilidade de ser alterado no decorrer do tempo deverá ser tratado como uma variável

- Quando um dado não tem nenhuma possibilidade de variar no decorrer do tempo, deverá ser tratado como constante

Exemplo: calcular a área de um triângulo. Sabemos que a fórmula para o cálculo da área de um triângulo é BASE \* ALTURA / 2. Base e altura são dados que irão variar no decorrer do “tempo de execução”. O número 2 da fórmula é um dado constante, pois sempre terá o mesmo valor

### Tipo de variáveis

- Inteiros: valores positivos ou negativos, que não possuem uma parte fracionária. Exemplos: 1, 30, 40, 12, -50

- Float (real): valores positivos ou negativos, que podem possuir uma parte fracionária (também podem ser inteiros). Exemplos: 1.4, 6.7, 10.3, 100, -47

- Caracteres (char ou string): qualquer elemento presente no teclado. Exemplos: “Maria”, “João”, ‘M’, ‘F’

- Lógico (boleano): verdadeiro ou falso. Exemplos: true, false, 1, 0

### Integer variables

```python
numero = -3
numero_jogos = 14
numero_convidados = 15
print(f'{numero}\n{numero_jogos}\n{numero_convidados}')
```

### Float Variables(floating point)

```python
pi = 3.14
numero_euler = 2.71
escala_terremoto = -4.55
print(f'{pi}\n{numero_euler}\n{escala_terremoto}')
```

### Strings and chars

```python
letra = 'a'
palavra1 = "linguagem de programação"
palavra2 = 'Python'
print(f'letra="{letra}"\npalavra1="{palavra1}"\npalavra2="{palavra2}"')
print(f'{letra} {palavra1}')
print('Estou aprendendo uma', palavra1)
print('Esta', palavra1, 'se chama', palavra2)
```

### Usando input()

```python
idade = int(input('Digite sua idade: '))
print('Sua idade é', idade)


pH= float(input('Qual o pH so solo durante a última medição? '))
print('O pH medido foi', pH)


nome=str(input('Qual o seu nome? '))
print('Seu nome é', nome)

```
