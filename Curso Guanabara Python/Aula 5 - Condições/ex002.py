velocidade = float(input('A quantos km o carro percorreu? '))

if velocidade > 80:
    print(f'Você foi multado! A multa sera de R${(velocidade - 80) * 7:.2f}')
else:
    print(f'Você esta dentro do limite!')