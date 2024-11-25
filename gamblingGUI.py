import json
import gamblingAccountLogin
from gamblingAccountLogin import *
from random import choice
from random import randint
import pygame
pygame.init()
window = pygame.display.set_mode([1920, 1080])

textFont = pygame.font.SysFont("Arial", 30)

global programPage, clickTimer, bankAccount, accountUsername

accountUsername = "Guest"

bankAccount = 1000
wheel1 = randint(1, 7)
wheel2 = randint(1, 7)
wheel3 = randint(1, 7)
deckOfCards = []
dealersHand = []
playersHand = []
gameInProgress = False
accountEntered = False
accountMade = False


def drawText(text, colour, x, y):
    img = textFont.render(text, True, colour)
    window.blit(img, (x, y))




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
    
    with open("gamblerAccounts.json", "w") as file:
        json.dump(file_data, file, indent = 4)





InteractList = [[],[]]

class Button():
    def __init__(self, name, x, y, width, height, colour, text):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.inUse = False
        self.text = text
        self.InteractType = "button"
        InteractList[0].append(self)
        
        
    def draw(self):
        if self.inUse == True:
            pygame.draw.rect(window, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))
            if self.text[0] != "none":
                drawText(self.text[0], self.text[1], self.text[2], self.text[3])
            
    def clicked(self):
        global programPage, aceValueAssigned, clickTimer, bankAccount, deckOfCards, cardsInDeck, dealersHand, dealersHandAmount, dealersHandValue, playersHand, playersHandAmount, playersHandValue, gameInProgress, gameStatus
        if clickTimer <= 0:
            for interacts in InteractList[1]:
                interacts.inputFinished = False
                interacts.active = False
            
            
            
            match self.name:

                case "Back":
                    
                    for inputBoxes in InteractList[1]:
                        inputBoxes.text[0] = "none"
                    
                    match programPage:
                        case "Account Menu" | "Gambling Menu":
                            programPage = "Main Menu"
                            
                        case "Login Menu" | "Register Menu":
                            programPage = "Account Menu"

                        case "Blackjack" | "Slots" | "Nim":
                            programPage = "Gambling Menu"

                case "EnterAccount":
                    programPage = "Account Menu"
                
                case "BeginGambling":
                    programPage = "Gambling Menu"

                case "blackjackStart":
                    programPage = "Blackjack"
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
                    gameInProgress = True
                    cardsInDeck = len(deckOfCards)
                    gameStatus = "Ongoing"
                    aceValueAssigned = True
                    
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

                    playersHandValue = 0
                    for i in range(playersHandAmount):
                        if playersHand[i][2] != "ace":
                            playersHandValue += playersHand[i][2]
                        else:
                            aceValueAssigned = False
                            
                    if aceValueAssigned == False:
                        blackjackAceHighButton.inUse = True
                        blackjackAceLowButton.inUse = True
                                    
                    if gameStatus == "Win" or gameStatus == "Loss":
                        updateBalance(bankAccount)
                                

                    dealersHandValue = 0
                    for i in range(dealersHandAmount):
                        if dealersHand[i][2] != "ace":
                            dealersHandValue += dealersHand[i][2]
                        else:
                            aceValue = randint(1,2)
                            if aceValue == 1:
                                dealersHandValue += 1
                            elif aceValue == 2:
                                dealersHandValue += 11
                                
                    if playersHandValue == 21:
                        if playersHandValue > dealersHandValue:
                            bankAccount += 1000
                            gameStatus = "Win"
                            gameInProgress = False
                        
                        else:
                            bankAccount -= 1000
                            gameStatus = "Loss"
                            gameInProgress = False        
                    
                case "AccountLogin":
                    programPage = "Login Menu"
                    
                case "AccountRegister":
                    programPage = "Register Menu"
                    
                case "accountDetailsSubmit":
                    global accountEntered, gamblerAccounts, bankAccountNumber, currentGamblerAccount, accountMade, accountUsername
                    if programPage == "Login Menu":
                        loginAttempt = accountLoginGUI(LoginInputUsernameButton.text[0], LoginInputPasswordButton.text[0])
                        if loginAttempt == "success":
                            currentGamblerAccount = gamblingAccountLogin.currentGamblerAccount
                            accountUsername = currentGamblerAccount
                            accountEntered = True
                            with open("gamblerAccounts.json", "r+") as file:
                                file_data = json.load(file)
                                gamblerAccounts = file_data["gambler_accounts"]
                                bankAccount = gamblingAccountLogin.gamblerBalance
                                bankAccountNumber = gamblingAccountLogin.accountArrayLocation
                                
                    elif programPage == "Register Menu":
                        registerAttempt = accountRegistrationGUI(RegisterInputUsernameButton.text[0], RegisterInputPasswordButton.text[0], RegisterInputPasswordConfirmButton.text[0])
                        if registerAttempt == "success":
                            accountMade = True
                                
                    
                case "blackjackHit":
                    cardDrawn = randint(1, cardsInDeck)
                    for i in range(1, cardsInDeck+1):
                        if i == cardDrawn:
                            cardDrawn = deckOfCards[i-1]
                            del deckOfCards[i-1]
                            playersHand.append(cardDrawn)
                            break
                    cardsInDeck = len(deckOfCards)
                    playersHandAmount = len(playersHand)

                    playersHandValue = 0
                    for i in range(playersHandAmount):
                        if playersHand[i][2] != "ace":
                            playersHandValue += playersHand[i][2]
                        else:
                            aceValueAssigned = False
                                    
                    if playersHandValue == 21:
                        if playersHandValue > dealersHandValue:
                            bankAccount += 1000
                            gameStatus = "Win"
                            gameInProgress = False
                        
                        else:
                            bankAccount -= 1000
                            gameStatus = "Loss"
                            gameInProgress = False
                            
                    elif playersHandValue > 21:
                        bankAccount -= 1000
                        gameStatus = "Loss"
                        gameInProgress = False
                        
                    if gameStatus == "Win" or gameStatus == "Loss":
                        updateBalance(bankAccount)
                        
                case "blackjackStand":
                    
                    
                    if playersHandValue > dealersHandValue:
                        bankAccount += 1000
                        gameStatus = "Win"
                        gameInProgress = False
                        
                    else:
                        bankAccount -= 1000
                        gameStatus = "Loss"
                        gameInProgress = False
                        
                    if gameStatus == "Win" or gameStatus == "Loss":
                        updateBalance(bankAccount)
                        
                case "blackjackAceLow":
                    playersHandValue += 1
                    aceValueAssigned = True
                
                case "blackjackAceHigh":
                    playersHandValue += 11
                    aceValueAssigned = True

                case "slotsStart":
                    programPage = "Slots"

                case "slotsRoll":
                    global wheel1, wheel2, wheel3
                    wheel1 = randint(1, 7)
                    wheel2 = randint(1, 7)
                    wheel3 = randint(1, 7)
                    if wheel1 == 7 and wheel2 == 7 and wheel3 == 7:
                        amountWon = int(500)
                        bankAccount = bankAccount + amountWon 

                    elif (4 < wheel1 and 4 < wheel2 and 4 < wheel3):
                        amountWon = int(50)
                        bankAccount = bankAccount + amountWon

                    elif (4 <= wheel1 <= 7 and 4 <= wheel2 <= 7) or (4 <= wheel1 <= 7 and 4 <= wheel3 <= 7) or (4 <= wheel2 <= 7 and 4 <= wheel3 <= 7):
                        amountWon = int(20)
                        bankAccount = bankAccount + amountWon

                    else:
                        bankAccount = bankAccount - 50

                case "nimStart":
                    programPage = "Nim"

            clickTimer = 80


textFont = pygame.font.SysFont("Arial", 40)
BackButton = Button("Back", 1700, 900, 100, 100, (255, 0, 0), ("Back", (255, 255, 255), 1710, 920))
BeginGamblingButton = Button("BeginGambling", 760, 700, 400, 150, (255, 0 , 0), ["Start Gambling", (255, 255, 255),850, 725])
EnterAccountButton = Button("EnterAccount", 350, 700, 400, 150, (0,0,200), ["Login/Register", (255, 255, 255),450, 725])

AccountLoginButton = Button("AccountLogin", 450, 700, 400, 150, (0,0,200), ["Login", (255, 255, 255),600, 725])
AccountRegisterButton = Button("AccountRegister", 1070, 700, 400, 150, (0,0,200), ("Register", (255, 255, 255),1220, 725))

accountDetailsSubmitButton = Button("accountDetailsSubmit", 860, 820, 200, 100, (0, 150, 0), ["Enter", (255,255,255),900, 830])


blackjackStartButton = Button("blackjackStart", 760, 700, 400, 150, (0,0,255), ["Play Blackjack", (255, 255, 255),850, 725])
blackjackHitButton = Button("blackjackHit", 450, 700, 400, 150, (0,0,200), ["Hit", (255, 255, 255),600, 725])
blackjackStandButton = Button("blackjackStand", 1070, 700, 400, 150, (0,0,200), ["Stand", (255, 255, 255),1220, 725])
blackjackAceLowButton = Button("blackjackAceLow", 700, 600, 75, 50, (225, 20, 225), ["Low", (255, 255, 255), 710, 600])
blackjackAceHighButton = Button("blackjackAceHigh", 800, 600, 75, 50, (225, 20, 225), ["High", (255, 255, 255), 810, 600])


slotsStartButton = Button("slotsStart", 350, 700, 400, 150, (0,0,255), ["Play Slots", (255, 255, 255),470, 725])
slotsRollButton = Button("slotsRoll", 710, 700, 500, 150, (0,0,255), ["Roll", (255, 255, 255),920, 725])
slotsWheel1Button = Button("slotsWheel1", 710, 400, 100, 100, (100, 0, 155), [str(wheel1), (255, 255, 255), 750, 425])
slotsWheel2Button = Button("slotsWheel2", 910, 400, 100, 100, (100, 0, 155), [str(wheel2), (255, 255, 255), 950, 425])
slotsWheel3Button = Button("slotsWheel3", 1110, 400, 100, 100, (100, 0, 155), [str(wheel3), (255, 255, 255), 1150, 425])

nimStartButton = Button("nimStart", 1170, 700, 400, 150, (0,0,255), ["Play Nim Type Zero", (255, 255, 255),1230, 725])




class InputBox():
    def __init__(self, name, x, y, width, height, colour, text):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.inUse = False
        self.text = text
        self.active = False
        self.InteractType = "Input Box"
        self.inputFinished = False
        self.inputText = ""
        InteractList[1].append(self)
        
        
    def draw(self):
        if self.inUse == True:
            pygame.draw.rect(window, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))
            if self.text[0] != "none":
                drawText(self.text[0], self.text[1], self.text[2], self.text[3])
            
    def clicked(self):
        global programPage, clickTimer, bankAccount, deckOfCards, cardsInDeck, dealersHand, dealersHandAmount, dealersHandValue, playersHand, playersHandAmount, playersHandValue, gameInProgress, wheel1, wheel2, wheel3
        if clickTimer <= 0:
            for interacts in InteractList[1]:
                interacts.inputFinished = False
                interacts.active = False
            
            
            match self.name:           
                    
                case "LoginInputUsername":
                    LoginInputUsernameButton.active = True
                    
                case "LoginInputPassword":
                    LoginInputPasswordButton.active = True
                    
                case "RegisterInputUsername":
                    RegisterInputUsernameButton.active = True
                    
                case "RegisterInputPassword":
                    RegisterInputPasswordButton.active = True
                    
                case "RegisterInputPasswordConfirm":
                    RegisterInputPasswordConfirmButton.active = True
        
    def inputFinishedFunc(self, inputText):
        self.inputText = inputText
        

        

LoginInputUsernameButton = InputBox("LoginInputUsername", 760, 450, 400, 100, (0, 0, 200), ["none", (255, 255, 255),760, 475])
LoginInputPasswordButton = InputBox("LoginInputPassword", 760, 650, 400, 100, (0, 0, 200), ["none", (255, 255, 255),760, 675])

RegisterInputUsernameButton = InputBox("RegisterInputUsername", 760, 400, 400, 100, (0, 0, 200), ["none", (255, 255, 255),760, 425])
RegisterInputPasswordButton = InputBox("RegisterInputPassword", 760, 550, 400, 100, (0, 0, 200), ["none", (255, 255, 255),760, 575])
RegisterInputPasswordConfirmButton = InputBox("RegisterInputPasswordConfirm", 760, 700, 400, 100, (0, 0, 200), ["none", (255, 255, 255),760, 725])

programPage = "Main Menu"
clickTimer = 0


run = True
while run:
    if clickTimer > 0:
        clickTimer -=1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            
        for inputBoxes in InteractList[1]:
            if inputBoxes.active == True:
                if event.type == pygame.KEYDOWN: 
                    
        
                    if event.key == pygame.K_BACKSPACE: 
                        
                        inputBoxes.text[0] = inputBoxes.text[0][:-1] 
        
                    elif event.key == pygame.K_RETURN:
                        inputBoxes.inputFinished = True
                        inputBoxes.inputFinishedFunc(inputBoxes.text[0])
        
                    else: 
                        if inputBoxes.text[0] != "none":
                            inputBoxes.text[0]  += event.unicode
                        else: 
                            inputBoxes.text[0] = event.unicode
            
    window.fill((155, 155, 155))
    mouseX, mouseY = pygame.mouse.get_pos()

    drawText(f"Account: {accountUsername}", (255, 255, 255), 200, 25)
    drawText(f"Bank Account: {bankAccount}", (255, 255, 255),1600, 25)
    
    
    for interacts in InteractList[0] + InteractList[1]:
        
        if interacts.x < mouseX < interacts.x + interacts.width and interacts.y < mouseY < interacts.y + interacts.height and interacts.inUse == True and pygame.mouse.get_pressed()[0]:
            if clickTimer <= 0:
                match interacts.name:
                    case "slotsRoll":
                        interacts.clicked()
                        slotsWheel1Button = Button("slotsWheel1", 710, 400, 100, 100, (100, 0, 155), (str(wheel1), (255, 255, 255), 750, 425))
                        slotsWheel2Button = Button("slotsWheel2", 910, 400, 100, 100, (100, 0, 155), (str(wheel2), (255, 255, 255), 950, 425))
                        slotsWheel3Button = Button("slotsWheel3", 1110, 400, 100, 100, (100, 0, 155), (str(wheel3), (255, 255, 255), 1150, 425))
                    
                    case _: #basically the else of switch statements
                        interacts.clicked()
            else:
                interacts.clicked()
        interacts.draw()
        interacts.inUse = False

    if programPage != "Main Menu" and gameInProgress == False and accountMade == False:
        BackButton.inUse = True

    match programPage:

        case "Main Menu":
            BeginGamblingButton.inUse = True
            EnterAccountButton.inUse = True

        case "Account Menu":
            AccountLoginButton.inUse = True
            AccountRegisterButton.inUse = True
            
        case "Login Menu":
            LoginInputUsernameButton.inUse = True
            LoginInputPasswordButton.inUse = True
            if accountEntered == False and accountMade == False:
                accountDetailsSubmitButton.inUse = True
                
        case "Register Menu":
            RegisterInputUsernameButton.inUse = True
            RegisterInputPasswordButton.inUse = True
            RegisterInputPasswordConfirmButton.inUse = True
            if accountEntered == False and accountMade == False:
                accountDetailsSubmitButton.inUse = True
            else:
                drawText("Please close and re-open program to access new account (Press escape)", (255, 255, 255), 560, 825)

        case "Gambling Menu":
            blackjackStartButton.inUse = True
            slotsStartButton.inUse = True
            nimStartButton.inUse = True

        case "Blackjack":
            if aceValueAssigned != False:
                blackjackHitButton.inUse = True
                blackjackStandButton.inUse = True
            drawText("BLACKJACK", (255, 255, 255),910, 25)
            drawText(f"Current cards: {playersHand}",(20, 20, 255),450, 425)
            drawText(f"Current Hand Value: {playersHandValue}",(20, 20, 255),450, 525)
            if aceValueAssigned == True:
                drawText(f"Cards in Deck: {cardsInDeck}",(20, 255, 20), 450, 325)
            if gameStatus == "Win":
                drawText("You win!", (255, 255, 255), 900, 100)
                drawText(f"Dealer's hand: {dealersHand}",(255, 20, 20),450, 225)
                drawText(f"Dealer's hand Value: {dealersHandValue}",(255, 20, 20),450, 175)
            elif gameStatus == "Loss":
                drawText("You lose!", (255, 255, 255), 700, 100)
                drawText(f"Dealer's hand: {dealersHand}",(255, 20, 20),450, 225)
                drawText(f"Dealer's hand Value: {dealersHandValue}",(255, 20, 20),450, 175)
                
            if aceValueAssigned == False:
                blackjackAceHighButton.inUse = True
                blackjackAceLowButton.inUse = True
                
                

        case "Slots":
            slotsRollButton.inUse = True
            slotsWheel1Button.inUse = True
            slotsWheel2Button.inUse = True
            slotsWheel3Button.inUse = True
            drawText("SLOTS", (255, 255, 255),910, 25)

    
    
    pygame.display.update()
    
pygame.quit()