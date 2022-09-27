
x = 0.4   # answer is 0.0632455532
epsilon = 0.0001    
numGuesses = 0
low = x   # 0.0
high = 1  # x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))
print(ans, "squared is", ans**2)
