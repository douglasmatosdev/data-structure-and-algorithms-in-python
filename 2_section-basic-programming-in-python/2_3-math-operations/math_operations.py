# Math Operations
import math

a = 5
b = 3
print(f'a={a}\nb={b}')

print(f'A soma de {a} + {b} = {a + b}')
print(f'A subtração de {a} - {b} = {a - b}')
print(f'A divisão de {a} / {b} = {a / b}')
print(f'A multiplicação de {a} * {b} = {a * b}')
print(f'A resto da divisão 10 / 3 = {10 % 3}')
print('5 * 5 * 5 * 5 =', 5 * 5 * 5 * 5)
print(f'5 elevado à 4 é 5**4 =', 5**4)
print(math.sqrt(9))

# Arredonamento
casos_doenca = 134
numero_habitantes = 34432
casos_por_habitante = casos_doenca / numero_habitantes

# Sem arredondamento
print(casos_por_habitante)

# Com arredondamento de 6 casas decimais
print(round(casos_por_habitante, 6))

# Com arredondamento de 4 casas decimais
print('O número de casos por habitante é de', round(casos_por_habitante, 4))
