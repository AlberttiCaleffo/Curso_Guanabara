# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA\n',
      '-=' * 10)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão do PA: '))
contador = 0
contador2 = 0

while contador < 10:
    print(f'{primeiro_termo}', end=' -> ')
    contador += 1
    primeiro_termo += razao
    if contador == 10:
        print('Pause')
        mais_termos = int(input('Quantos termos mostrar a mais? '))
        contador2 += mais_termos + contador
        while mais_termos:
            while contador < contador2:
                print(f'{primeiro_termo}', end=' -> ')
                contador += 1
                primeiro_termo += razao
            print('Pause')
            mais_termos = int(input('Quantos termos mostrar a mais? '))
            contador2 += mais_termos
print(f'Programa finalizado. Termos usados: {contador2}')