from rich import print
from time import sleep
import os
import sys

"""
Schéma fichier

First_part_text / time_to_speech,delay,color | Second_part / time_to_speech,delay,color/(\\n)
"""

def clear():
    if sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")

def import_lyrics(file):
    lyric = []
    with open(file,"r") as f:
        for line in f.readlines():
            line_fsplit = line.split("|")
            for l in line_fsplit:
                line_split = l.split("/")
                parameter = line_split[1].split(",")
                
                #calcule du delay char parameter[0]
                parameter[0] = float(parameter[0]) / len(line_split[0])
                
                if len(line_split) == 2:
                    lyric.append((line_split[0], float(parameter[0]), float(parameter[1]), parameter[2], False))
                else:
                    lyric.append((line_split[0], float(parameter[0]), float(parameter[1]), parameter[2], True))
        return lyric

def print_lyrics(lyrics):
    clear()
    for i, (lyric, delay_char, delay, color, line_break) in enumerate(lyrics):
        for char in lyric:
            print(f"[{color}]{char}[/{color}]",end="")
            sleep(delay_char)
        if line_break:
            print()
        sleep(delay)

clear()
sleep(3)
print_lyrics(import_lyrics("debug.txt"))