# 2. Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem,
# utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo,
# o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela.
# Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO \* VELOCIDADE.
# Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem,
# com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média,
# tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem

km_por_litro = 12
time = float(input('Informe o tempo gasto:'))
speed = float(input('Informe a velocidade média:'))
distancia = time * speed
litros_usados = distancia / km_por_litro

print()

print('Velocidade média:', speed)
print('Tempo gasto:', time)
print('Distância percorrida:', distancia)
print('Quantida de litros utilizados:', round(litros_usados))
