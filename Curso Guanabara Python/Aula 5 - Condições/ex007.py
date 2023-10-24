salario = float(input('Digite o salario do funcionario: '))

if salario <= 1250.00:
    print(f'O salario de {salario} com o aumento de 15% é de R${salario + (salario * 0.15):.2f}')
else:
    print(f'O salario de {salario} com o aumento de 10% é de R${salario + (salario * 0.10):.2f}')