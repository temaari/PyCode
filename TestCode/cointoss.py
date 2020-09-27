import random

def printCoin(side, a): #side is a string which holds heads or tails usually and a is the ascii value
    print ()
    print ("\t  ",a,a,a,a)
    print ("\t ",a,"     ",a)
    print ("\t",a,side,a)
    print ("\t",a,"       ",a)
    print ("\t ",a,"     ",a)
    print ("\t  ",a,a,a,a)

while (True):
    
    numHeads = 0
    numTails = 0
    asc = '#' #if you want to change the character
    #asc = input(" Enter An ASCII Character: ")
    bestOf = 1 #if you want to change number of coins
    #bestOf = int(input(" Enter Number of Coins: "))
    coins = bestOf #Used to keep atrack of the number of coins
    
    while (bestOf > 0):
        heads = 0
        tails = 0
        #Randomize upto 10 times
        value = random.randint(0,1)
        for i in range(10):	
            if 1 == value:	
                heads += 1
            else:
                tails += 1
        #Display Coin with number of heads, tails and ties
        if heads > tails:
            numHeads += 1
        elif heads < tails:
            numTails += 1
        bestOf -= 1
    
    print ()
    if (coins != 1):
        print ("\tHeads",numHeads,"Tails",numTails)
    for h in range(numHeads):
        printCoin(" HEADS ", asc)
    for t in range(numTails):
        printCoin(" TAILS ", asc)
    print ()
    input(" If You Would Like To Toss Again Press Enter!!")


