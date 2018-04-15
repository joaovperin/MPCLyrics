#!/usr/bin/python

import sys

import argparse

print ("Hello! Argv:")

parser = argparse.ArgumentParser(description='Obtains an prints the lyric for the song playing on MPD/Mopidy.')
parser.add_argument('--verbose', '-v', dest='verbose', action='count',
                   help='Specify if needs to echo everything.')

args = parser.parse_args()

print (args)

print(sys.argv)

verbose = args.verbose
print("Is verbose: " + str(verbose))

#verbose = len(sys.argv) >= 2 and str(sys.argv[1]) == 'verbose'
#print(verbose)
