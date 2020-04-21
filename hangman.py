'''

Author : Saurabh Kumbhar
Dated : 21 April 2020

'''

################################ H A N G M A N ################################

# Used to get random word
import random

#printing Rules
def printRules():
    
    #opening file in read mode rules.txt
    f = open('rules.txt','r')
    
    #loop line by line
    for lines in f:
        
        #printing each line in file
        print(lines)
        
        
#loading file containing words 
def load():
    
    #getting words in empty list
    words = []
    
    #Opening words.txt in read mode
    f = open('words.txt','r')
    
    #getting file line by line as each line contains different word
    for line in f:
        
        #getting word more than len 10
        if(len(line) > 10):
            
            #appending word in list
            words.append(line)
    
    #loading words    
    print("loading "+str(len(words))+" words...")
    
    #returning list of words
    return words

#to return random word
def getRandomWord():
    
    #getting list of words
    words = load()
    
    #getting random number between 0 and number of words
    randomNumber = random.randint(0,len(words))
    
    #returning random word
    return words[randomNumber]

#getting indexes of letter present in word 
def getIndexes(word,letter):
    
    #assigning empty list
    indexes = []
    
    #looping till length word
    for i in range(len(word)):
        
        #Comparing each letter of word with guess
        if(word[i] == letter):
            
            #getting index of matched letters
            indexes.append(i)
    
    #returning indexes of matched letter in word
    return indexes

#Printing Dashes
def printDashes(word,guesses):
    
    #Assigning counter to -1
    cnt = -1
    
    #loop through the word 
    for i in word:
        
        #getting all guesses           
        for j in guesses:
           
           #if guessed letter is equal to letter in word
           if(i == j):
               
               #printing letter if equal
               print(i,end="")
               
               #counter = 1
               cnt = 1
               break
           
           #else assigning counter 0
           else:
               cnt = 0
        
        #if counter is 0 print dash
        if(cnt == 0):
            print(" _ ",end="")

#Checking if all guesses matches word
def check(word,guesses):
    
    #Assigning counter 0
    cnt = 0
    
    #As if user enter same letter 2 times 
    #so making guesses distinct list 
    guesses = list(set(guesses))
    
    #looping through guesses 
    for guess in guesses:
        
        #looping through word
        for w in word:
        
            #if word is equal to guess
            if(w == guess):

                #increase counter by 1
                cnt+=1
    
    #if guesses are correct then counter will be equal to length           
    if(cnt == len(word)):
        return True

    return False
    
    
#Main Function
def main():
    
    #printing rules of GAME
    printRules()
    
    #getting random word as word is in format \nword\n
    word = getRandomWord()[::-2]
    
    #printing dashes of len of word
    for i in range(len(word)-1):
        print(" _ ",end = "")
    
    #Total chances is 8
    chance = 8
    print("\n You have "+str(chance)+" chances left.")
    
    #Assigning empty guesses
    guesses = []
    
    # As word is in format \nword
    word = word[1:]
    
    #Printing word to be guessed For Testing Purpose
    #print("Word to be guessed : ",word)
    
    #Loop till GAME Ends
    while(True):
        
        #Checking if guesses and word
        if(check(word,guesses)):
            print("Yeaaah You won the game")
            break
        
        #checking if chance left is 0 and word and guesses
        elif(check(word,guesses) == False and chance == 0):
            print("Game Over")
            break
        
        else:
            
            #Getting letter from user as Guess
            guessLetter = input("Enter your guess : ")
            
            #Appending guess in guesses
            guesses.append(guessLetter)
            
            #Getting indices
            Indices = getIndexes(word,guessLetter)
            
            #if matched indices is 0 lower the chance as guess is wrong
            if(len(Indices) == 0):
                chance-=1
            
            #print dashes and word guessed
            printDashes(word,guesses)
            
            #Printing number of chances left
            print("\n\n You have "+str(chance)+" chances left.")

#Calling Main Function    
main()


##############################  T E S T I N G ################################

'''
runfile('C:/Users/admin/Downloads/Python Project/hangman.py', 
wdir='C:/Users/admin/Downloads/Python Project')
************** H A N G M A N **************

Instructions

1. You have 8 chances.

2. You have to guess the letters.

3. If letter is contained in word it will be displayed.

4. If you guess wrong letter your chance will be reduced.

5. If you guess the word you will win the game.



loading 167514 words...
 _  _  _  _  _  _  _ 
 You have 8 chances left.
Word to be guessed :  osrorta

Enter your guess : a
 _  _  _  _  _  _ a

 You have 8 chances left.

Enter your guess : o
o _  _ o _  _ a

 You have 8 chances left.

Enter your guess : r
o _ ror _ a

 You have 8 chances left.

Enter your guess : r
o _ ror _ a

 You have 8 chances left.

Enter your guess : s
osror _ a

 You have 8 chances left.

Enter your guess : b
osror _ a

 You have 7 chances left.

Enter your guess : c
osror _ a

 You have 6 chances left.

Enter your guess : t
osrorta

 You have 6 chances left.
Yeaaah You won the game

runfile('C:/Users/admin/Downloads/Python Project/hangman.py', 
wdir='C:/Users/admin/Downloads/Python Project')
************** H A N G M A N **************

Instructions

1. You have 8 chances.

2. You have to guess the letters.

3. If letter is contained in word it will be displayed.

4. If you guess wrong letter your chance will be reduced.

5. If you guess the word you will win the game.



loading 167514 words...
 _  _  _  _  _  _  _ 
 You have 8 chances left.

Enter your guess : a
 _  _  _  _  _  _  _ 

 You have 7 chances left.

Enter your guess : b
 _  _  _  _  _  _  _ 

 You have 6 chances left.

Enter your guess : e
 _  _  _  _  _ e _ 

 You have 6 chances left.

Enter your guess : r
 _  _  _  _  _ e _ 

 You have 5 chances left.

Enter your guess : s
 _  _  _  _  _ e _ 

 You have 4 chances left.

Enter your guess : c
 _  _  _ c _ e _ 

 You have 4 chances left.

Enter your guess : o
 _  _  _ c _ e _ 

 You have 3 chances left.

Enter your guess : i
 _ i _ c _ e _ 

 You have 3 chances left.

Enter your guess : m
 _ i _ c _ e _ 

 You have 2 chances left.

Enter your guess : n
 _ inc _ e _ 

 You have 2 chances left.

Enter your guess : l
linc _ e _ 

 You have 2 chances left.

Enter your guess : d
lincde _ 

 You have 2 chances left.

Enter your guess : r
lincde _ 

 You have 1 chances left.

Enter your guess : u
lincde _ 

 You have 0 chances left.
Game Over

'''