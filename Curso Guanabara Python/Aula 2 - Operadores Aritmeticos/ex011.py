km = float(input('Digite a quantidade de km percorridos com o carro: '))
alugado = int(input('Por quantos dias foi alugado? '))
diaria = 60
km_taxa = 0.15
print(f'O valor total a pagar é R${(diaria * alugado) + (km_taxa * km):.2f}')