
low = 0
high = 100
ans = (high + low)//2
c = ''
               
print("Please think of a number between 0 and 100!")
while c != 'c':
    print("Is your secret number " + str(ans) + "?") 
    
    c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
  
    if c == 'l':
        low = ans
        ans = (high + low)//2
    elif c == 'h':
        high = ans
        ans = (high + low)//2
    elif c == 'c':
        print("Game over. Your secret number was:", ans)         
    else: 
        print("Sorry, I did not understand your input.")
      
 
    
##      TESTCASE 
####### find any number between 0 and 100 (not inclusive)
# for x in range(0, 100):
#     low = 0
#     high = 100
#     ans = (high + low)//2
#     #print("top ans", ans)
#     numGuesses = 0
#     # print("x:", x)
#     while abs(ans - x) >= epsilon:
#         # print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
#         #input()
#         numGuesses += 1
#         if ans < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low)//2
#         #print("bottoom ans", ans)
#     # print('numGuesses = ' + str(numGuesses))
#     print(str(ans) + ' equal to ' + str(x))
 