numero = int(input('Digite um numero a qual vai ser dada a tabuada: '))
tabuada = range(1, 11)
for a in tabuada:
    print(f'{numero} x {a} = {numero * a}')
