import math

ljustint=40

epsilon = float(input("Set Epsilon: ".ljust(ljustint+1)))


cube = float(input("Finde cube root of which number: ".ljust(ljustint+1)))
while cube != 0:
    if cube == "":
        exit
    num_guesses = 1
    low = 0.0
    high = cube
    guess = (high + low) / 2.0

    while abs(guess**3 - cube ) >= epsilon and num_guesses<50000:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.00
        num_guesses += 1

    print("Number of guesses:".ljust(ljustint), num_guesses)
    print("Cuberoot by bisectionSearch:".ljust(ljustint), round(guess,3))
    print("Exact cuberoot:".ljust(ljustint),math.cbrt(cube))
    print("")
    
    cube = float(input("Finde cube root of which number: ".ljust(ljustint+1)))