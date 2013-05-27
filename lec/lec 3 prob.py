# lecture 3.6, slide 2
# bisection search for square root


low = 0
high = 100
ans = (high + low)/2
print ('Please think of a number between 0 and 100!')
while True:
    print ('Is your secret number '+str(ans)+'?')
    us=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if us == 'l':
        low = ans
        ans = (high + low)/2
    elif us=='h':
        high = ans
        ans = (high + low)/2
    elif us=='c':
        break
    else:
        print('Sorry, I did not understand your input.')
print('Game over. Your secret number was: ' +str(ans))
