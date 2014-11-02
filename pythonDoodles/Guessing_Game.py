# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# initialize global variables used in your code
randnum = 100
counter = 7
def init():
    f.start()
    range100()
    
    

# define event handlers for control panel
    
def range100():
    global randnum
    global counter
    randnum = random.randrange(0,101)
    print "New Game! guess a number from 0 to 100"
    print "You have only 7 guesses"
    print " "  
    counter = 7

    # button that changes range to range [0,100) and restarts

def range1000():
    global randnum
    global counter
    randnum = random.randrange(0,1001)
    print "New Game! guess a number from 0 to 1000"
    print "You have only 10 guesses"
    print " "  
    counter = 10
    
    # button that changes range to range [0,1000) and restarts
    
def get_input(strguess):
    guess = int(strguess)
    global counter
    if counter != 0:
        if guess > randnum:
                      
            print "Guess was ", guess
            print "Lower!"            
            counter = counter - 1
            print "Number of remaining guesses: ",counter
            print " "  
        elif guess < randnum:
            print "Guess was ", guess
            print "Higher!"
            counter = counter - 1 
            print "Number of remaining guesses: ",counter
            print " "
        else:
            print "Guess was ", guess
            print "Your Guess is correct the number is ", randnum
            print "At ",counter, "guesses "
            print " "   
            init()
       
    else:
        print "You're out of required guesses. The number is ",randnum
        print " "
        init()
        
        
    
    
    
        
      

    # main game logic goes here	

    
# create frame

f = simplegui.create_frame("Guess the number",200,200)
f.add_button("0 to 100",range100, 100)
f.add_button("0 to 1000",range1000, 100)
f.add_input("Enter",get_input,100)

init()


# register event handlers for control elements


# start frame


# always remember to check your completed program against the grading rubric
