#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  
# Ex:                                                                                                                                                                        
# escreva(‘Olá, Mundo!’) Saída:                                                                                                                          
# ~~~~~~~~~                                                                                                                                                            
# Olá, Mundo!                                                                                                                                                          
# ~~~~~~~~~                                                                          

def escreva(msg):
    print('~' * (len(msg) + 3))
    print(f' {msg}  ')
    print('~' * (len(msg) + 3))
    
escreva('Ola, Mundo!') 
escreva('Curso de python bom')   