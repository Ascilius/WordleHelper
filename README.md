# WordleHelper

Inspired by [3Blue1Brown's video on Wordle](https://youtu.be/v68zYyaEmEA?si=aPSFk0ggaAB_bWmU).

Usage: ``python3 WordleHelper.py``

For each guess, enter the letters in their specific position that are green, yellow, and grey (in that order).
e.g. The guess "RAMEN":
```
Green Letters: _____ 
Yellow Letters: RA_E_
Grey Letters: __M_N
```
resulted in no green letters, (R, A, E) as yellow letters, and (M, N) as grey letters.

The program will then calculate which words are possible and recommend them to you.

### v1.1
 - updated README.md
 - reorganized files

### todo
 - improve UI
 - improve win/loss detection
 - improve word suggestions
    - implement entropy
 - add new words list
 - add player statistics

I use this to (sometimes) cheat in Wordle
![](./data/ah_eto.gif)
