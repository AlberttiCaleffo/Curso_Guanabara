def leiaDinheiro(valor= input('Digite um valor: ').strip()):
    while True:
        if valor.replace(',', '.').replace('.', '').isnumeric():
            return float(valor.replace(',', '.'))
        else:
            print('Erro, valor invalido!')
            valor = input('Digite um valor novamente: ')