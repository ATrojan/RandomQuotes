#***Random Quote Generator***
#Read a file and add each line as a list item
#Then upon hitting enter will select a random
#Line from that file and display it
#Written by A.Trojan


import random #import random number generator

x = 1

#file.txt is the file holding data change to name of your file
#store file.txt in same location as script

with open('file.txt', 'r') as f: #Opens text file and sets it to read

    quotes = f.readlines()    #Reads lines in file.txt and stores them in a list called data
    count = len(quotes)   #Counts number of items in text file/list
    
    #print count    #Prints number of items in the list
    #print data     #Prints List

    while x == 1:

        print 'Hit Enter for a Random Quote!'
        user = raw_input()  #Waits for user input

        if user.lower() == "exit": #Exit Loop and program
            x = 0  #Exits Loop

        else:
            ran = random.randrange(0,count, 1) #creates a random number between 0 and the number of items in quotes list.
            print quotes[ran]   #Print Random quote.

        
    
