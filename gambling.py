import json
import gamblingAccountLogin
from gamblingAccountLogin import *
from random import randint
from tkinter import *

global bankAccount


############ HAND CLASSES ARE A WORK IN PROGRESS #############
class AiHand:
    def __init__(self):
        self.hand = []
        
AiHands = []


def updateBalance(bankAccount):
    accountUsername = currentGamblerAccount
    with open("gamblerAccounts.json", "r") as file:
        file_data = json.load(file)
    
    accountFound = False
    for account in file_data["gambler_accounts"]:
        if account["account_username"] == accountUsername:
            account["balance"] = bankAccount
            accountFound = True
            break
    
    if accountFound == False:
        print("Account not found")
    with open("gamblerAccounts.json", "w") as file:
        json.dump(file_data, file, indent = 4)

    print("Balance for", accountUsername, "successfully updated to", bankAccount)

def drawCard(hand, deckOfCards, cardsInDeck):
    cardDrawn = randint(1, cardsInDeck)
    for i in range(1, cardsInDeck+1):
        if i == cardDrawn:
            cardDrawn = deckOfCards[i-1]
            del deckOfCards[i-1]
            hand.append(cardDrawn)
            break
    cardsInDeck = len(deckOfCards)
    return hand, deckOfCards, cardsInDeck

def placeCard(cardPos, hand, playedCards):
    cardPlaced = hand[cardPos]
    playedCards.append(cardPlaced)
    del hand[cardPos]
    print(f"Card {cardPlaced} has been placed")


def slots():
    global bankAccount
    print("You are using the slot machine")
    amountGambled = int(input("How much money are you wanting to gamble? "))
    if 0 < amountGambled < 1000:
        print("You have chosen to gamble", amountGambled)
        wheel1 = randint(1, 7)
        wheel2 = randint(1, 7)
        wheel3 = randint(1, 7)
        print(wheel1, wheel2, wheel3)
        if wheel1 == 7 and wheel2 == 7 and wheel3 == 7:
            amountWon = int(amountGambled)
            print("Congrats, you have won", amountWon)
            bankAccount = bankAccount + amountWon 
            print("You now have", bankAccount)
        elif (4 < wheel1 and 4 < wheel2 and 4 < wheel3):
            amountWon = int(amountGambled * 0.25)
            print("Congrats, you have won", amountWon)
            bankAccount = bankAccount + amountWon
            print("You now have", bankAccount)
        elif (4 <= wheel1 <= 7 and 4 <= wheel2 <= 7) or (4 <= wheel1 <= 7 and 4 <= wheel3 <= 7) or (4 <= wheel2 <= 7 and 4 <= wheel3 <= 7):
            amountWon = int(amountGambled * 0.1)
            print("Congrats, you have won", amountWon)
            bankAccount = bankAccount + amountWon
            print("You now have", bankAccount)
        else:
            bankAccount = bankAccount - amountGambled
            print("Better luck next time!")
            print("You now have", bankAccount)
    elif amountGambled > 1000:
        print("Please pick a lower amount")
    else:
        print("Please pick a valid number")
    updateBalance(bankAccount)
    
def blackjack():
    global bankAccount
    deckOfCards = [("ace", "spades", "ace"), ("two", "spades", 2), ("three", "spades", 3), ("four", "spades", 4), ("five", "spades", 5),
                    ("six", "spades", 6), ("seven", "spades", 7), ("eight", "spades", 8), ("nine", "spades", 9), ("ten", "spades", 10), ("jack", "spades", 10),
                    ("queen", "spades", 10), ("king", "spades", 10),  ("ace", "clubs", "ace"), ("two", "clubs", 2), ("three", "clubs", 3), ("four", "clubs", 4),
                    ("five", "clubs", 5), ("six", "clubs", 6), ("seven", "clubs", 7), ("eight", "clubs", 8), ("nine", "clubs", 9), ("ten", "clubs", 10),
                    ("jack", "clubs", 10), ("queen", "clubs", 10), ("king", "clubs", 10),  ("ace", "hearts", "ace"), ("two", "hearts", 2), ("three", "hearts", 3),
                    ("four", "hearts", 4), ("five", "hearts", 5), ("six", "hearts", 6), ("seven", "hearts", 7), ("eight", "hearts", 8), ("nine", "hearts", 9),
                    ("ten", "hearts", 10), ("jack", "hearts", 10), ("queen", "hearts", 10), ("king", "hearts", 10),  ("ace", "diamonds", "ace"), ("two", "diamonds", 2), 
                    ("three", "diamonds", 3), ("four", "diamonds", 4), ("five", "diamonds", 5), ("six", "diamonds", 6), ("seven", "diamonds", 7), ("eight", "diamonds", 8), 
                    ("nine", "diamonds", 9), ("ten", "diamonds", 10), ("jack", "diamonds", 10), ("queen", "diamonds", 10), ("king", "diamonds", 10),]
    dealersHand = []
    playersHand = []
    amountGambled = int(input("How much do you wish to bet"))
    if 0 < amountGambled < bankAccount:
        cardsInDeck = len(deckOfCards)
        gameInProgress = True

        dealersHandAmount = len(dealersHand)
        dealersHandValue = 0
        while dealersHandAmount < 2:
            dealersHand, deckOfCards, cardsInDeck = drawCard(dealersHand, deckOfCards, cardsInDeck)
            dealersHandAmount = len(dealersHand)

        playersHandAmount = len(playersHand)
        playersHandValue = 0
        while playersHandAmount < 2:
            playersHand, deckOfCards, cardsInDeck = drawCard(playersHand, deckOfCards, cardsInDeck)
            playersHandAmount = len(playersHand)


        while gameInProgress == True:
            playersHandValue = 0
            for i in range(playersHandAmount):
                if playersHand[i][2] != "ace":
                    playersHandValue += playersHand[i][2]
                else:
                    aceValue = input("Is your ace low or high?")
                    if aceValue.lower() == "low":
                        playersHandValue += 1
                    elif aceValue.lower() == "high":
                        playersHandValue += 11

            dealersHandValue = 0
            for i in range(dealersHandAmount):
                if dealersHand[i][2] != "ace":
                    dealersHandValue += dealersHand[i][2]
                else:
                    aceValue = randint(1,2)
                    if aceValue == 1:
                        value = 1
                    elif aceValue == 2:
                        value = 11
            
            print("Your current hand is", playersHand, ", worth", playersHandValue)
            if playersHandValue < 21:
                turnDecision = input("Do you wish to hit or stand")
                if turnDecision.lower() == "hit":
                    playersHand, deckOfCards, cardsInDeck = drawCard(playersHand, deckOfCards, cardsInDeck)
                    playersHandAmount = len(playersHand)
                if turnDecision.lower() == "stand":
                    print("You have", playersHandValue, "with", playersHandAmount, "cards") 
                    print("The dealer had a hand value of", dealersHandValue, "with", dealersHandAmount, "cards")
                    if playersHandValue > dealersHandValue:
                        amountWon = int(amountGambled)
                        bankAccount = bankAccount + amountWon
                        print("You win!")
                        print("You now have", bankAccount)
                        gameInProgress = False
                    else:
                        bankAccount = bankAccount - amountGambled
                        print("Better luck next time!")
                        print("You now have", bankAccount)
                        gameInProgress = False
            elif playersHandValue == 21:
                print("You have", playersHandValue, "with", playersHandAmount, "cards")
                print("The dealer had a hand value of", dealersHandValue, "with", dealersHandAmount, "cards")
                if playersHandValue > dealersHandValue:
                    bankAccount = bankAccount + amountGambled
                    print("You win!")
                    print("You now have", bankAccount)
                    gameInProgress = False
                else:
                    print("Dealer wins due to House Advantage")
                    bankAccount = bankAccount - amountGambled
                    print("Better luck next time")
                    print("You now have", bankAccount)
                    gameInProgress = False
            else:
                print("You have gone bust, with a hand containing", playersHandAmount,"cards, with a combined value of", playersHandValue)
                print("The dealer had a hand value of", dealersHandValue)
                bankAccount = bankAccount - amountGambled
                print("Better luck next time!")
                print("You now have", bankAccount)
                gameInProgress = False
        updateBalance(bankAccount)
            
    else:
        print("Please enter a valid amount")


def nimTypeZero():
    global bankAccount
    deckOfCards = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
    cardsInDeck = len(deckOfCards)
    playedCards = []
    playersHand = []
    aiPlayers = 3
    AiHands = []
    for i in range(aiPlayers):
        AiHands.append(AiHand())
    for aiHand in AiHands:
        for i in range(4):
            aiHand.hand, deckOfCards, cardsInDeck = drawCard(aiHand.hand, deckOfCards, cardsInDeck)
    for i in range(4):
        playersHand, deckOfCards, cardsInDeck = drawCard(playersHand, deckOfCards, cardsInDeck)
    print(f"Your current hand is {playersHand}")
    


accountEntered = False

while accountEntered == False:
    newPlayer = input("Do you have an account set up? ")
    if newPlayer.lower() == "no":
        accountRegistration()
    elif newPlayer.lower() == "yes":
        accountLogin()
        currentGamblerAccount = gamblingAccountLogin.currentGamblerAccount
        accountEntered = True
    else: 
        print("Sorry, please input a valid answer")

with open("gamblerAccounts.json", "r") as file:
    file_data = json.load(file)
    gamblerAccounts = file_data["gambler_accounts"]

bankAccount = gamblingAccountLogin.gamblerBalance
print("Your balance is", bankAccount)
bankAccountNumber = gamblingAccountLogin.accountArrayLocation


playingAgain = "yes"
stillGambling = "yes"
while bankAccount > 0 and stillGambling == "yes":
    stillGambling = input("Are you still wanting to gamble? ")
    if stillGambling.lower() == "yes":
        playingAgain = "yes"
        gamblingChoice = input("What game/machine are you wanting to use/play? ")
        if gamblingChoice.lower() == "slots" or gamblingChoice.lower() == "slot machine":
            while playingAgain == "yes":
                slots(bankAccount)
                playingAgain = input("Are you wanting to play again? ")
                

        elif gamblingChoice.lower() == "blackjack" or gamblingChoice.lower() == "21":
            print("You are playing 21")
            while playingAgain == "yes":
                blackjack()    
                playingAgain = input("Are you wanting to play again? ")  
                
        elif gamblingChoice.lower() == "nim":
            print("You are playing nim type zero")
            while playingAgain == "yes":
                nimTypeZero()
                playingAgain = input("Are you wanting to play again? ")  
            
        else:
            print("please enter a valid option")
