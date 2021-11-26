#!/usr/bin/python

import sys
import random
from termcolor import cprint
import os

#responsive dont work :(
rows = os.popen('tput cols').read()
width = int(rows)

gameWatchColor = 'grey'
fontColors = ['yellow','green','blue','cyan','red','magenta']
fontColor = random.choice(fontColors)

gameWatch = [
"              -______           ",
"            >+\//////\\_-       ",
"           >|///////////\_      ",
"    ----   \/////////////+>|||> ",
"  -+///\_  \/////////////|_///< ",
"  -/////\  _\///////////|<      ",
"   >+++|/|< -<|//|++++>-        ",
"       -<|/||||//||_>    ->>>-  ",
"          >|////////\>>>+\///|> ",
"  --      -_\/////////////////< ",
" <//_   -_/////////+     >___-  ",
" >|//\_+\/+>-----+\+            ",
"  -|///\|>        +\+>          ",
"    <<<>         +\///++>       ",
"                 <______-       "]

gwTitle = [
"  _____        __      ____      _      __     __      __  ",
" / ___/__  ___/ /__   / __/___  | | /| / /__ _/ /_____/ /  ",
"/ /__/ _ \/ _  / -_)  > _/_ _/  | |/ |/ / _ `/ __/ __/ _ \ ",
"\___/\___/\_,_/\__/  |_____/    |__/|__/\_,_/\__/\__/_//_/ "]

mrTitle = [
"   __  ___     ",
"  /  |/  /_    ",
" / /|_/ / __/  ",
"/_/  /_/_/ (_) "]



def blanks(num):
    for i in range(num):
        print(" ",end="")


if width > len(gameWatch[0]):
    for i in range(len(gameWatch)):
        diff = len(gameWatch)-len(mrTitle)
        if i < diff:
            blanks(len(mrTitle[0])+2)
            cprint(gameWatch[i],gameWatchColor,attrs=['bold'])
        else:
            blanks(2)
            cprint(mrTitle[i-diff],fontColor,attrs=['bold'],end="")
            cprint(gameWatch[i],gameWatchColor,attrs=['bold'])

    for i in range(len(gwTitle)):
        blanks(2)
        cprint(gwTitle[i],fontColor,attrs=['bold'])
else:
    for i in range(len(gameWatch)):
        blanks(2)
        cprint(gameWatch[i],gameWatchColor,attrs=['bold'])

   
print()
print()
