import random

def test_integer():
    t = True
    while t:        
        number = raw_input()
        if number.isdigit():
            if int(number) == 1 or int(number) == 2 or int(number) == 3 or int(number) == 4 or int(number) == 5 or int(number) == 6 or int(number) == 7 or int(number) == 8:
                t = False
            else:
                print " I said a number between 1 and 8, Dummkopf!"
        else:
            print " I said a number between 1 and 8, Dummkopf!"
    return int(number)
    

# program
turn = 0
red = 0

secret = []

#secret
for i in range(1, 5):
    secret.append(random.randrange(1, 9, 1))
print secret    


print " Bonjour Monsieur Poulpe, time to use your neurons!"


while red < 4:
    # guess
    turn = turn + 1
    print " Make a guess for the first number (between 1 and 8)"
    a = test_integer()
    print " Make a guess for the second number (between 1 and 8)" 
    b = test_integer()
    print " Make a guess for the third number (between 1 and 8)"
    c = test_integer()
    print " Make a guess for the last number (between 1 and 8)"
    d = test_integer()
    
    guess = [a,b,c,d]
    print "Your guess is ", [a,b,c,d]
    
    red = 0
    white = 0
    red_place = [0,1,2,3] 
    white_place = [0,1,2,3] 

    # checking for the first red
    for i in range(0, 4):        
        if guess[i] == secret[i]: 
            red_place.remove(i)    
            white_place.remove(i)
            red = red + 1 
        if red == 4:
            print " There we go! T'es trop fort!    >0     =0    >0    =0 "
            print " And you made it in ", turn, "turn(s)."
            print " Allez, go back to Landscape xx"
                
    # checking for whites        
 
    for j in red_place:
        for h in white_place:
            if guess[j] == secret[h]: 
                white_place.remove(h)
                white = white + 1
                break
            
    # result
     
    if red == 0 and white == 0:        
        print " Ca m'est saucisson mais quand meme, t'es trop nul! try again"
    elif red == 0 and white == 1 or red==0 and white == 2:
        print " Das Leben ist kein Ponyhof, you've got",red,'red and',white,'white'
    elif red == 2:
        print " Getting better! You've got",red,'red and',white,'white'
    elif red == 3:
        print " Almost. ALMOST! You've got",red,'red and',white,'white!'
    else:
        print " You've got",red,'red and',white,'white' 
        
    


