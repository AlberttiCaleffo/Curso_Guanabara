numero = int(input('Digite um numero inteiro: '))

print('''Escolha umas das bases: 
      [ 1 ] converter para BINARIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEADECIMAL''')
escolha = int(input('Qual opção: '))

if escolha == 1:
    print(f'O numero {numero} convertido em BINARIO é: {bin(numero)[2:]}')
elif escolha == 2:
    print(f'O numero {numero} convertido em OCTAL é: {oct(numero)[2:]}')
else:
    print(f'O numero {numero} convertido em HEXADECIMAL é: {hex(numero)[2:]}')