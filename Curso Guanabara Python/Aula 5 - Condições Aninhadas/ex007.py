# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

primeiro_segmento = int(input('Primeiro segmento: '))
segundo_segmento = int(input('Segundo segmento: '))
terceiro_segmento = int(input('Terceiro segmento: '))

soma_1 = primeiro_segmento + segundo_segmento
soma_2 = primeiro_segmento + terceiro_segmento

if soma_1 > terceiro_segmento and soma_2 > segundo_segmento and primeiro_segmento == segundo_segmento and primeiro_segmento == terceiro_segmento:
    print('É possivel criar um triangulo e ele é um EQUILÁTERO!')
elif soma_1 > terceiro_segmento and soma_2 > segundo_segmento and primeiro_segmento == segundo_segmento or segundo_segmento == terceiro_segmento or primeiro_segmento == terceiro_segmento:
    print('É possivel criar um triangulo e ele é um ISÓSCELES!')
elif soma_1 > terceiro_segmento and soma_2 > segundo_segmento and primeiro_segmento != segundo_segmento and primeiro_segmento != terceiro_segmento and segundo_segmento != terceiro_segmento:
    print('É possivel criar um triangulo e ele é um ESCALENO!')
else:
    print('Não é possivel fazer um triangulo.')