# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar

# [ 2 ] multiplicar

# [ 3 ] maior

# [ 4 ] novos números

# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
print('=-' * 10)
operacao = int(input('Escolha uma das opções:\n'
                     '[1] Somar\n'
                     '[2] Multiplicar\n'
                     '[3] Maior\n'
                     '[4] Novos números\n'
                     '[5] Sair do programa '))
while operacao in range(1, 5) or operacao not in range(1, 5):
    if operacao == 1:
        print(f'A soma dos dois numeros é {numero_1 + numero_2}')
    elif operacao == 2:
        print(f'A multiplicação dos dois numeros é {numero_1 * numero_2}')
    elif operacao == 3:
        if numero_1 > numero_2:
            print(f'O maior numero é {numero_1}')
        else:
            print(f'O maior numero é {numero_2}')
    elif operacao == 4:
        numero_1 = int(input('Digite o primeiro numero: '))
        numero_2 = int(input('Digite o segundo numero: '))
    elif operacao == 5:
        break
    elif operacao not in range(1, 5):
        print(f'Valor invalido. Insira novamente a operação:')
        sleep(2)
    print('=-' * 10)   
    operacao = int(input('Escolha uma das opções:\n'
                         '[1] Somar\n'
                         '[2] Multiplicar\n'
                         '[3] Maior\n'
                         '[4] Novos números\n'
                         '[5] Sair do programa '))
print('Finalizando programa...\n')
sleep(3)
print('Programa finalizado.')
