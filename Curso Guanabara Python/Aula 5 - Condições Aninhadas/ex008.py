# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso

# – Entre 18,5 e 25: Peso Ideal

# – 25 até 30: Sobrepeso

# – 30 até 40: Obesidade

# – Acima de 40: Obesidade Mórbida

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:  
    print(f'Seu imc é {imc:.1f} e você esta abaixo do peso.')
elif imc > 18.5 and imc <= 25:
    print(f'Seu imc é {imc:.1f} e seu peso é o IDEAL!')
elif imc > 25 and imc < 30:
    print(f'Seu imc é {imc:.1f} e você esta no sobrepeso!')
elif imc > 30 and imc < 40:
    print(f'Seu imc é {imc:.1f} e você esta obeso!')
elif imc > 40:
    print(f'Seu imc é {imc:.1f} e OBESIDADE MÓRBIDA!')