viagem_km = float(input('Digite os kms da viagem: '))

if viagem_km <= 200:
    print(f'O valor da viagem ficou R${viagem_km * 0.50:.2f}')
else:
    print(f'O valor da viagem com desconto saiu R${viagem_km * 0.45:.2f}')