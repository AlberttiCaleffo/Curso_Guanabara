# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

times = ('Botafogo', 'Flamengo', 'Grêmio', 'Fluminese', 'Palmeiras', 'Bragantino', 'Fortaleza', 'São Paulo',
         'Cruzeiro', 'Internacional', 'Athletico-PR', 'Atlético-MG', 'Santos', 'Cuiabá', 'Corinthians',
         'Bahia', 'Goiás', 'Coritiba', 'Vasco da Gama', 'América-MG')

print(times[0:5])
print(times[-4:])
print(sorted(times))
print(times.index('Coritiba'))