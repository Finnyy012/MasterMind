import itertools
import random

kleuren = [1,2,3,4,5,6]
duplicates = True
max_guesses = 10
guesses = []
current = 1
lengte = 4
potential = []

def get_feedback(guess, code):
    kopie_guess = list(guess)
    kopie_code = list(code)

    b = 0
    w = 0

    for i in range(lengte):
        if (kopie_code[i] == kopie_guess[i]):
            b += 1
            kopie_code[i] = 'X'
            kopie_guess[i] = 'Y'
            print(kopie_code)

    for i in range(lengte):
        if kopie_guess[i] in kopie_code:
            w += 1

    return [b,w]

def get_column():
    fb_col = []
    b = 0
    w = len(kleuren)-1
    while b<(lengte-1):
        for j in range(w):
            fb_col.append([b,j])
        b+=1
        w-=1
    fb_col.append([b,0])
    fb_col.append([b+1,0])
    return fb_col

print(get_column())