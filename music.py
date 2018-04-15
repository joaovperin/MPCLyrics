
import requests
import sys
from PyLyrics import *
import os
import re
import subprocess
import time

import argparse

# Adds Command line args
parser = argparse.ArgumentParser(description='Obtains an prints the lyric for the song playing on MPD/Mopidy.')
parser.add_argument('--verbose', '-v', dest='verbose', action='count', help='Specify if needs to echo everything.')

# Parses the Cmd Line Args
args = parser.parse_args()

# Prints if verbose above that level
def printV(text):
    if (args.verbose >= 1):
        print("*** " + str(text))

# Retorna a música e o arista tocando no momento
def getCurrentPlayingSongAndArtist():
    song, artist = '', ''
    ## Salva nome do artista
    os.system('mpc -f %artist% current > artist.txt')
    with open('artist.txt', 'r') as myfile:
        artist = myfile.read().replace('\n', '')

    ## Salva nome da Musica
    os.system('mpc -f %title% current > song.txt')
    with open('song.txt', 'r') as myfile:
        song = myfile.read().replace('\n', '')
    return [song, artist]

# Busca e printa a letra de uma música dado o artista
def printLyrics(song, artist):
    # Limpa a tela e printa o nome da música
    if (args.verbose == 0):
        os.system('clear')
    print("\n\n\n")
    print("Current Song: '" + str(song) + "' - Current Artist: '" + str(artist) + "'.\n")

    lyrics = ''
    try:
        lyrics = PyLyrics.getLyrics(artist,song)
    except TypeError:
        lyrics = 'Song or Artist not found'
    except:
        lyrics = 'A error ocurred, sorry.'
    # Printa letra da musica
    print(lyrics)

# Starts the application main loop
printV ("Starting application...")
song, artist, new_song, new_artist = '', '', '', ''

# Main Loop
while True:
    (new_song, new_artist) = getCurrentPlayingSongAndArtist()
    printV("Current Song: '" + str(new_song) + "' - Current Artist: '" + str(new_artist) + "'.")
    # Verifica se a musica mudou e se mudou chama a funcao de printar as letra
    if song != new_song and artist != new_artist:
        printV("Changing song from '" + str(song) +"' to '" + str(new_song) + "'.")
        (song, artist) = (new_song, new_artist)
        printLyrics(song, artist)
    time.sleep(3)
#End.
