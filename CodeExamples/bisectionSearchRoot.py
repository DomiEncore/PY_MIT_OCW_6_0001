
epsilon = float(input("Set Epsilon: "))


cube = float(input("Finde cube root of which number: "))
while cube != 0:
    if cube == "":
        exit
    num_guesses = 1
    low = 0.0
    high = cube
    guess = (high + low) / 2.0

    while abs(guess**3 - cube ) >= epsilon:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.00
        num_guesses += 1
    print(round(guess,3), '  (', num_guesses,')')
    print("")
    
    cube = float(input("Finde cube root of which number: "))