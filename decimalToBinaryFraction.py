
# Note below code handles numbers greater than 1 as well
# Try 3.375
x = float(input('Enter a decimal number between 0 and 1: '))
# Try 0.375 , 0.1 , 0.2 , 0.5

p = 0
while ((2**p)*x)%1 != 0:
    print("(top 2**p)*x:",(2**p)*x)
    print("int((2**p)*x)):", int((2**p)*x))
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1
    print("(bottom 2**p)*x:",(2**p)*x)

print("The power exponent:",p)
num = int(x*(2**p))
print("num:", num)


## This is just decimal to binary conversion e.g. 3 to 11
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

print("result:", result)
print("p - len(result):", p - len(result))
# if p = 2 , we need to shift 2 decimal of a binary number , 
# and so on , p = 5 , to shift 5 decimal.
#  
# for loop to shift right
for _ in range(p - len(result)):
    # Why is the right most bit always 0 ?
    # Well it's not always e.g. dec 0.5 is bin .1
    result = '0' + result     # shift right e.g. 11 becomes 011
print("result after right shift :", result)

# 0:-p This is for numbers > 1 e.g. 3.375 is 11.011
# -p: is the whole string after the binary point
result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))
