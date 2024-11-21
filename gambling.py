import json
import gamblingAccountLogin
from gamblingAccountLogin import *
from random import randint
from random import choice
from tkinter import *

global bankAccount
global accountUsername


class AiHand:
    def __init__(self):
        self.hand = []
        self.safeHand = []
        nameChoices = ["Steve", "Mishel", "Billy", "Libby", "George", "Finley", "Ethan", "Charlie", "Tio", "Sophie", "Katelyn", "Joseph", "Amy", "Reece", "Shauna"]
        self.name = choice(nameChoices)
AiHands = []


def updateBalance(bankAccount):
    global accountUsername
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
    return cardPos, hand, playedCards


def slots():
    global bankAccount
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
                    ("six", "spades", 6), ("seven", "spades", 7), ("eight", "spades", 8), ("nine", "spades", 9), ("ten", "spades", 10), 
                    ("jack", "spades", 10),("queen", "spades", 10), ("king", "spades", 10),  ("ace", "clubs", "ace"), ("two", "clubs", 2), 
                    ("three", "clubs", 3), ("four", "clubs", 4),("five", "clubs", 5), ("six", "clubs", 6), ("seven", "clubs", 7),
                    ("eight", "clubs", 8), ("nine", "clubs", 9), ("ten", "clubs", 10),("jack", "clubs", 10), ("queen", "clubs", 10),
                    ("king", "clubs", 10),  ("ace", "hearts", "ace"), ("two", "hearts", 2), ("three", "hearts", 3),("four", "hearts", 4),
                    ("five", "hearts", 5), ("six", "hearts", 6), ("seven", "hearts", 7), ("eight", "hearts", 8), ("nine", "hearts", 9),
                    ("ten", "hearts", 10), ("jack", "hearts", 10), ("queen", "hearts", 10), ("king", "hearts", 10),  ("ace", "diamonds", "ace"),
                    ("two", "diamonds", 2), ("three", "diamonds", 3), ("four", "diamonds", 4), ("five", "diamonds", 5), ("six", "diamonds", 6),
                    ("seven", "diamonds", 7), ("eight", "diamonds", 8), ("nine", "diamonds", 9), ("ten", "diamonds", 10), ("jack", "diamonds", 10), 
                    ("queen", "diamonds", 10), ("king", "diamonds", 10),]
    dealersHand = []
    playersHand = []
    amountGambled = int(input("How much do you wish to bet? "))
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
    accountUsername = currentGamblerAccount
    deckOfCards = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
    cardsInDeck = len(deckOfCards)
    playedCards = []
    playersHand = []
    orderOfPlay = []
    aiPlayers = 3
    AiHands = []
    amountGambled = int(input("How much do you wish to bet? "))
    if 0 < amountGambled < bankAccount:
        gameInProgress = True

        for i in range(aiPlayers):
            AiHands.append(AiHand())

        for aiHand in AiHands:
            for i in range(aiPlayers+1):
                aiHand.hand, deckOfCards, cardsInDeck = drawCard(aiHand.hand, deckOfCards, cardsInDeck)

        for i in range(aiPlayers+1):
            playersHand, deckOfCards, cardsInDeck = drawCard(playersHand, deckOfCards, cardsInDeck)
        
        print(f"Your current hand is {playersHand}")
        orderOfPlay.append(accountUsername)
        for aiHand in AiHands:
            orderOfPlay.append(aiHand.name)
        print(orderOfPlay)
        
        while gameInProgress == True:
            playedCardsValue = 0
            for i in range(len(orderOfPlay)):
                if gameInProgress == True:
                    playedCardsValue = 0
                    if orderOfPlay[i] == accountUsername:
                        cardPlaced = int(input(f"What card do you want to play? Your current cards are: {playersHand}. Choose by position in list.")) - 1
                        cardPlaced, playersHand, playedCards = placeCard(cardPlaced, playersHand, playedCards)
                    else:
                        for aiHand in AiHands:
                            if orderOfPlay[i] == aiHand.name:
                                for j2 in range(len(playedCards)):
                                    playedCardsValue += playedCards[j2]

                                for card in range(len(aiHand.hand)):
                                    if not (aiHand.hand[card] + playedCardsValue >= 9):
                                        aiHand.safeHand.append(aiHand.hand[card])

                                if len(aiHand.safeHand)  >= 1:
                                    cardPlaced = randint(0, len(aiHand.safeHand)-1)
                                    #these 4 lines basically fix the safe hand positioning so that its in the correct part of the normal hand and it therefore picks the right card
                                    #basically teaches the ai the difference between the cards it can place down this turn and NOT die, and the ones thatll just lose it this turn
                                    cardPlaced = aiHand.safeHand[cardPlaced]
                                    for card in range(len(aiHand.hand)):
                                        if aiHand.hand[card] == cardPlaced:
                                            cardPlaced = card
                                            break

                                else:
                                    cardPlaced = randint(0, len(aiHand.hand)-1)

                                cardPlaced, aiHand.hand, playedCards = placeCard(cardPlaced, aiHand.hand, playedCards) 
                                aiHand.safeHand = []
                                playedCardsValue = 0    

                    for j in range(len(playedCards)):
                        playedCardsValue += playedCards[j]
                    print(playedCards)
                    print(f"The current cards add up to {playedCardsValue}")

                    if playedCardsValue >= 9:
                        print(f"{orderOfPlay[i]} took the play pile count over 9, they lose")
                        if orderOfPlay[i] == accountUsername:
                            bankAccount = bankAccount - amountGambled
                            print("Better luck next time!")
                            print(f"You now have {bankAccount}")
                            updateBalance(bankAccount)
                            gameInProgress = False

                        else:
                            for aiHand in AiHands:
                                if orderOfPlay[i] == aiHand.name:
                                    bankAccount = bankAccount + amountGambled // 3
                                    print(f"{aiHand.name} has lost")
                                    updateBalance(bankAccount)
                                    gameInProgress = False
                                    break

def poker():
    global bankAccount
    deckOfCards = [("ace", "spades", "ace"), ("two", "spades", 2), ("three", "spades", 3), ("four", "spades", 4), ("five", "spades", 5),
                    ("six", "spades", 6), ("seven", "spades", 7), ("eight", "spades", 8), ("nine", "spades", 9), ("ten", "spades", 10), 
                    ("jack", "spades", 10),("queen", "spades", 10), ("king", "spades", 10),  ("ace", "clubs", "ace"), ("two", "clubs", 2), 
                    ("three", "clubs", 3), ("four", "clubs", 4),("five", "clubs", 5), ("six", "clubs", 6), ("seven", "clubs", 7),
                    ("eight", "clubs", 8), ("nine", "clubs", 9), ("ten", "clubs", 10),("jack", "clubs", 10), ("queen", "clubs", 10),
                    ("king", "clubs", 10),  ("ace", "hearts", "ace"), ("two", "hearts", 2), ("three", "hearts", 3),("four", "hearts", 4),
                    ("five", "hearts", 5), ("six", "hearts", 6), ("seven", "hearts", 7), ("eight", "hearts", 8), ("nine", "hearts", 9),
                    ("ten", "hearts", 10), ("jack", "hearts", 10), ("queen", "hearts", 10), ("king", "hearts", 10),  ("ace", "diamonds", "ace"),
                    ("two", "diamonds", 2), ("three", "diamonds", 3), ("four", "diamonds", 4), ("five", "diamonds", 5), ("six", "diamonds", 6),
                    ("seven", "diamonds", 7), ("eight", "diamonds", 8), ("nine", "diamonds", 9), ("ten", "diamonds", 10), ("jack", "diamonds", 10), 
                    ("queen", "diamonds", 10), ("king", "diamonds", 10),]
    playersHand = []
    orderOfPlay = []
    aiPlayers = 5
    AiHands = []

    amountGambled = int(input("How much do you wish to bet? "))




    


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
    stillGamblingCheck = input("Are you still wanting to gamble? ")
    if stillGamblingCheck.lower() == "yes":
        stillGambling = "yes"
        playingAgain = "yes"
        gamblingChoice = input("What game/machine are you wanting to use/play? ")


        if gamblingChoice.lower() == "slots" or gamblingChoice.lower() == "slot machine":
            while playingAgain == "yes":
                print("You are using the slot machine")
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
        
        elif gamblingChoice.lower() == "poker":
            print("You are playing poker")
            while playingAgain == "yes":
                poker()    
                playingAgain = input("Are you wanting to play again? ")  
            
        else:
            print("please enter a valid option")
    elif stillGamblingCheck.lower() == "no":
        stillGambling = "no"
    else:print("Please choose another option")