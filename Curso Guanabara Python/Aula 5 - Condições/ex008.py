reta_a = float(input('Digite a primeira reta: '))
reta_b = float(input('Digite a segunda reta: '))
reta_c = float(input('Digite a terceira reta: '))

if reta_a + reta_b > reta_c and reta_b + reta_c > reta_a:
    print(f'Ele consegue formar um triangulo!')
else:
    print(f'Ele NÃO consegue formar um triangulo!')