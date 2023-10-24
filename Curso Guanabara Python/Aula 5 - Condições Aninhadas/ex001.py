casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario do comprador: '))
quantos_anos = int(input('Em quantos anos vai pagar: '))
quantos_meses = quantos_anos * 12
prestacao = casa / quantos_meses

if prestacao >= salario * 0.30:
    print(f'O valor a pagar da casa é {casa:.2f} em {quantos_anos} anos e a prestação sera de {prestacao:.2f}\nEmprestimo NEGADO!')
else:
    print(f'O valro a pagar da casa é {casa:.2f} em {quantos_anos} anos e a prestação sera de {prestacao:.2f}\nEmprestimo APROVADO!')