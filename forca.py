import random

lista= ['FUTEBOL', 'JOGADOR', 'INSTAGRAM', 'BANANA'
        , 'YOUTUBE', 'COCIELO', 'CRISTIAN']

i = random.randint(0, len(lista)- 1)
palavra_secreta = lista[i]
#apagar a linha abaixo
print palavra_secreta
palavra_exibida = '-'*len(palavra_secreta)
print palavra_exibida
erros = 0
#comeca o loop do jogo
while( erros <7 and palavra_secreta != palavra_exibida):
    letra = raw_input('Digite uma letra: ')
    letra = letra.upper()
    tem_letra = 'nao'
    for i in palavra_secreta:
        if i == letra:
            tem_letra = 'sim'
    if tem_letra == 'nao':
        erros = erros + 1
    #else:

    print erros    
       
