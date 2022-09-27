
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:   # STEPS PASSED ANSWER 
    print("guess is", guess)
    if guess <= x:                  
        guess += step
    else:
        break                       #A ND CONTINOUS TO 23.000000000000057

if abs(guess**2 - x) >= epsilon:    # 506 - 23
    print('failed')
else:
    print('succeeded: ' + str(guess))