#!/usr/bin/env python
# coding: utf-8

# In[55]:



import random
class CustomException(Exception):
    pass
    
pair = [['scissors', 'paper'], ['rock', 'scissors'], ['paper', 'rock']]
items = ['rock', 'paper', 'scissors']

def choice():
    while (True):    
        try:
            userInput =  eval(input('Enter choice between 1, 2 or 3 indicating rock, paper, scissors respectively\n'))
            userInput  = userInput - 1
            if ((userInput < 0) or (userInput >2) ):
                raise CustomException()
        except (CustomException, ValueError) as e:
            print('Wrong input try again\n')
        else:    
            user = items[userInput]    
            com = items[random.randrange(3)]
            print ('CPU ('+com +')\nUser ('+user')')
            if (user == com):
                print('It\'s a draw play again')
                continue

            arr1 = [user, com]
            arr2 = arr1.reverse()



            for item in pair:
                if (arr1 == item):
                    return True
                elif (arr2 == item):
                    return False


# In[56]:


def play():
    terminate = 0
    while(terminate < 1):
        check = choice()
        if (check == True):
            print("********** User Wins! **********\n")
            terminate = int(input('Enter 0 to play again or 1 to terminate'))
        elif (check == False ):
            print("********** Com Wins! **********\n")
            terminate = int(input('Enter 0 to play again or 1 to terminate'))
            
play()





