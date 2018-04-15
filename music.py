
import requests
import sys
from PyLyrics import *
import os
import re
import subprocess
import time
artist = " "
song = " "
def pegaMusica():
    global song
    global artist
    ## Salva nome do artista
    os.system('mpc -f %artist% current > artist.txt')
    with open('artist.txt', 'r') as myfile:
        artist = myfile.read().replace('\n', '')

    ## Salva nome da Musica
    os.system('mpc -f %title% current > song.txt')
    with open('song.txt', 'r') as myfile:
        song = myfile.read().replace('\n', '')


def printaLetra():
    global song
    global artist
    ##limpa tela
    os.system('clear')
    print("\n\n\n\n\n\n\n\n")
    ## Printa nome da musica 
    pegaMusica()
    print(artist + " " +song + "\n")
    ## Printa letra da musica
    print(PyLyrics.getLyrics(artist,song))


def verificaMusica():
    global song
    global artist
    ##Busca musica novamente e salva em outra variavel para comparacao
    os.system('mpc -f %title% current > song.txt')
    with open('song.txt', 'r') as myfile:
        newsong=myfile.read().replace('\n', '')
    
    ##Verifica se a musica mudou e se mudou chama a funcao de printar as letras
    if song != newsong:
        song = newsong
        printaLetra()
        
        


# Verifica musica a cada 10 Segundos
while True:
    #print ("Verificando")
    verificaMusica()
    time.sleep(5)




