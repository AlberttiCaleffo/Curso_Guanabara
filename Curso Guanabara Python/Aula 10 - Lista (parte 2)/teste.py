numero = []
outro_n = []

for c in range(0, 5):
    outro_n.append(int(input('Digite um numero: ')))
    numero.append(outro_n[:])
    outro_n.clear()

print(numero)