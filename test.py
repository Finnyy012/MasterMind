import itertools
import random

kleuren = [1,2,3,4,5,6]
duplicates = True
max_guesses = 10
guesses = []
current = 1
lengte = 4
potential = []

def get_perms():
    if(duplicates):
        perms = itertools.product(kleuren, repeat=lengte)
    else:
        perms = itertools.permutations(kleuren, lengte)
    return [p for p in perms]


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

    for i in range(lengte):
        if kopie_guess[i] in kopie_code:
            w += 1
            kopie_code[kopie_code.index(kopie_guess[i])] = 'X'
            kopie_guess[i] = 'Y'

    return [b, w]



def get_column(guess):
    fb_col = []
    b = 0
    w = len(kleuren) - 1
    while b < (lengte - 1):
        for j in range(w):
            fb_col.append([b, j])
        b += 1
        w -= 1
    fb_col.append([b, 0])
    fb_col.append([b + 1, 0])

    res = []
    for i in range(len(fb_col)):
        res.append(0)

    for i in potential:
        fb = get_feedback(guess, i)
        for j in fb_col:
            if (j == fb):
                res[fb_col.index(j)] += 1
                break

    return res

def guess():
    matrix = []
    for i in potential:
        matrix.append(get_column(i))

    ex_sizes = []
    for i in matrix:
        ex = 0
        for j in i:
            ex += (j**2)/(len(kleuren)**lengte)

        ex_sizes.append(ex)

    return ex_sizes

potential = get_perms()
ex = 0
i = get_column(potential[7])
print(potential[7])
print(i)
for j in i:
    t = (j ** 2)
    ex += t
    print("t:  " + str(t))
    print("ex: " + str(ex))
ex = ex / (len(kleuren) ** lengte)
print(ex)

g = guess()
print(g)
print(min(g))
print(potential[g.index(min(g))])