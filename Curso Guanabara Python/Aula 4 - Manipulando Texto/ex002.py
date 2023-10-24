numero = int(input('Digite um numero de 0 a 9999: '))
milhar = numero // 1000
resto_milhar = numero % 1000
centena = resto_milhar // 100
resto_centena = resto_milhar % 100
dezena = resto_centena // 10
print(f'Unidade: {str(numero)[-1]} Dezena: {dezena} Centena: {centena} Milhar: {milhar}')