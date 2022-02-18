import itertools
import random

def play():
    # settings en zo
    kleuren = [1,2,3,4,5,6]
    duplicates = True
    max_guesses = 10
    lengte = 4

    current = 1
    potential = []

    # maakt een lijst met alle mogelijke antwoorden
    def get_perms():
        if(duplicates):
            perms = itertools.product(kleuren, repeat=lengte)
        else:
            perms = itertools.permutations(kleuren, lengte)
        return [p for p in perms]

    # geeft feedback in zwarte en witte pins aan de hand van een guess
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

        return [b,w]

    # maakt een random code
    def generate_code():
        if (duplicates):
            return list(random.choices(kleuren, k=lengte))
        else:
            return list(random.sample(kleuren, k=lengte))

    # elimineert alle onmogelijke antwoorden aan de hand van een nieuwe guess met feedback
    def eliminate(guess, fb):
        res = []
        for code in potential:
            if(fb == get_feedback(guess, code)):
                res.append(code)
        return res

    # maakt een colom met het aantal mogelijke codes waarvoor de guess de feedback zou krijgen die bij die index hoort
    def get_column(guess):
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

        res = []
        for i in range(len(fb_col)):
            res.append(0)

        for i in potential:
            fb = get_feedback(guess, i)
            for j in fb_col:
                if(j == fb):
                    res[fb_col.index(j)]+=1
                    break

        return res

    # zet de colommen om in expected values (met de formule uit het artikel)
    # en returnt de guess uit de mogelijke guesses met de laagste E[x]
    def get_guess():
        ex_sizes = []
        for i in potential:
            col = get_column(i)
            ex = 0
            for j in col:
                ex += (j ** 2) / (len(kleuren) ** lengte)
            ex_sizes.append(ex)

        return potential[ex_sizes.index(min(ex_sizes))]

    code = generate_code()
    print("code: " + str(code))
    potential = get_perms()

    # loop die het spel runt
    while True:
        ## haal comment weg om tegen de computer te spelen
        # guess = input("guess " + str(current) + "/" + str(max_guesses) + ": ")
        # guess = list(guess)
        # for i in range(len(guess)):
        #     guess[i] = int(guess[i])

        ## willekeurige guess strategie; gemiddeld 5.65 guesses uit 20000 runs
        # guess = potential[random.randint(0, len(potential) - 1)]

        ## eerstvolgende valide guess strategie; gemiddeld 6.77 guesses uit 20000 runs
        # guess = potential[0]

        ## expected size strategie; gemiddeld 5.472 guesses uit 500 runs (20000 duurde me iets te lang)
        guess = get_guess()

        print("guess " + str(current) + "/" + str(max_guesses) + ": " + str(guess))
        current += 1

        if(code == list(guess)):
            print("you win ^^")
            return current
        else:
            fb = get_feedback(guess, code)
            potential = eliminate(guess, fb)
            print(fb)

        if(current == max_guesses+1):
            print(code)
            print("you lose :(")
            return 0


play()

# #haal comment weg om gemiddeld aantal beurten te zien (kan even duren voor expected size strategy)
# a = 0
# for i in range(20000):
#     print(str(i) + "/20000")
#     a+=play()
# a=a/20000
# print(a)
