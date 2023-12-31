# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), 
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

# Exercício Python 108: Adapte o código do desafio #107, 
# criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), 
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. 
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, 
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), 
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilidadesCeV import moeda
from utilidadesCeV import dado

valor = dado.leiaDinheiro()
moeda.resumo(valor, 43, 20)