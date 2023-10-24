aument = 0
dimin = 0

def aumento(valor, formatar= False):
    if formatar:
        return valor * (dimin / 100) + valor
    else:
        return moeda(valor * (dimin / 100) + valor) 
    
def diminiucao(valor, formatar= False):
    if formatar:
        return valor - (valor * (aument / 100))
    else:
        return moeda(valor - (valor * (aument / 100)))
    
def dobro(valor, formatar= False):
    if formatar:
        return valor * 2
    else:
        return moeda(valor * 2)
    
def metade(valor, formatar= False):
    if formatar:
        return valor / 2
    else:
        return moeda(valor / 2)

def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def resumo(valor, aumentar, diminuir):
    global aument, dimin
    aument = aumentar
    dimin = diminuir
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}\n'
          f'Dobro do preço: \t{dobro(valor)}\n'
          f'Metade do preço: \t{metade(valor)}\n'
          f'{aumentar}% de aumento: \t{aumento(valor)}\n'
          f'{diminuir}% de redução: \t{diminiucao(valor)}')
    print('-' * 30)
    
    