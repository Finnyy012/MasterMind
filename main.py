import itertools
import random

def play():
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

        return [b,w]

    def generate_code():
        if (duplicates):
            return list(random.choices(kleuren, k=lengte))
        else:
            return list(random.sample(kleuren, k=lengte))


    def eliminate(guess, fb):
        res = []
        for code in potential:
            if(fb == get_feedback(guess, code)):
                res.append(code)
        return res

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


    def get_guess():
        matrix = []
        for i in potential:
            matrix.append(get_column(i))

        ex_sizes = []
        for i in matrix:
            ex = 0
            for j in i:
                ex += (j**2)/(len(kleuren)**lengte)
            ex_sizes.append(ex)

        return potential[ex_sizes.index(min(ex_sizes))]


    code = generate_code()
    print("code: " + str(code))
    potential = get_perms()


    while True:
        # guess = input("guess " + str(current) + "/" + str(max_guesses) + ": ")
        # guess = list(guess)
        # for i in range(len(guess)):
        #     guess[i] = int(guess[i])

        #guess = potential[random.randint(0, len(potential) - 1)]
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

a = 0
for i in range(500):
    a+=play()
a=a/500
print(a)
