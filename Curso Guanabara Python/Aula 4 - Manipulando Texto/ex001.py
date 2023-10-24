nome = input('Digite o seu nome completo: ')

print(f'''O nome com todas as letras maiusculas: {nome.upper()}
O nome com todas as letras minusculas: {nome.lower()}''')
print('Quantas letras ao todo: {}'.format(len(nome.replace(' ', ''))))
print(f'Quantas letras tem o primeiro nome: {len(nome.split()[0])}')