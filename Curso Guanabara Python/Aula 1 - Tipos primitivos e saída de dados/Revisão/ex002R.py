alguma_coisa = input('Digite qualquer coisa: ')

print(f'As seguintes verificações foram feitas: ')
print(f'''É um numero e alfabetico? {alguma_coisa.isalnum()}
É letra? {alguma_coisa.isalpha()}
É ascii? {alguma_coisa.isascii()}
É decimal? {alguma_coisa.isdecimal()}
É minusculo? {alguma_coisa.islower()}
É maisculo? {alguma_coisa.isupper()}
A primeira letra é maiscula? {alguma_coisa.istitle}''')