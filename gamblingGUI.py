#######################################
#THIS ENTIRE FILE IS A WORK IN PROGRESS
#######################################

from random import randint
import pygame
pygame.init()
window = pygame.display.set_mode([1920, 1080])

textFont = pygame.font.SysFont("Arial", 30)

bankAccount = 1000
wheel1 = randint(1, 7)
wheel2 = randint(1, 7)
wheel3 = randint(1, 7)


def drawText(text, colour, x, y):
    img = textFont.render(text, True, colour)
    window.blit(img, (x, y))


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
        ButtonList.append(self)
        
        
    def draw(self):
        if self.inUse == True:
            pygame.draw.rect(window, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))
            if self.text != "none":
                drawText(self.text[0], self.text[1], self.text[2], self.text[3])
            
    def clicked(self, programPage, clickTimer, bankAccount):
        if clickTimer <= 0:
            match self.name:

                case "Back":
                    match programPage:
                        case "Login Menu" | "Gambling Menu":
                            programPage = "Main Menu"

                        case "Blackjack" | "Slots" | "Nim":
                            programPage = "Gambling Menu"

                case "EnterAccount":
                    programPage = "Login Menu"
                
                case "BeginGambling":
                    programPage = "Gambling Menu"


                case "blackjackStart":
                    programPage = "Blackjack"
                


                case "slotsStart":
                    programPage = "Slots"

                case "slotsRoll":
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
                    return programPage, 80, bankAccount, wheel1, wheel2, wheel3

                case "nimStart":
                    programPage = "Nim"
        

        
        return programPage, 80, bankAccount

ButtonList = []
textFont = pygame.font.SysFont("Arial", 40)
BackButton = Button("Back", 1700, 900, 100, 100, (255, 0, 0), ("Back", (255, 255, 255), 1710, 920))
BeginGamblingButton = Button("BeginGambling", 760, 700, 400, 150, (255, 0 , 0), ("Start Gambling", (255, 255, 255),850, 725))
EnterAccountButton = Button("EnterAccount", 350, 700, 400, 150, (0,0,200), ("Login/Register", (255, 255, 255),450, 725))

AccountLoginButton = Button("AccountLogin", 450, 700, 400, 150, (0,0,200), ("Login", (255, 255, 255),600, 725))
AccountRegisterButton = Button("AccountRegister", 1070, 700, 400, 150, (0,0,200), ("Register", (255, 255, 255),1220, 725))

blackjackStartButton = Button("blackjackStart", 760, 700, 400, 150, (0,0,255), ("Play Blackjack", (255, 255, 255),850, 725))
blackjackHitButton = Button("blackjackHit", 450, 700, 400, 150, (0,0,200), ("Hit", (255, 255, 255),600, 725))
blackjackStandButton = Button("blackjackStand", 1070, 700, 400, 150, (0,0,200), ("Stand", (255, 255, 255),1220, 725))

slotsStartButton = Button("slotsStart", 350, 700, 400, 150, (0,0,255), ("Play Slots", (255, 255, 255),470, 725))
slotsRollButton = Button("slotsRoll", 710, 700, 500, 150, (0,0,255), ("Roll", (255, 255, 255),920, 725))
slotsWheel1Button = Button("slotsWheel1", 710, 400, 100, 100, (100, 0, 155), (str(wheel1), (255, 255, 255), 750, 425))
slotsWheel2Button = Button("slotsWheel2", 910, 400, 100, 100, (100, 0, 155), (str(wheel2), (255, 255, 255), 950, 425))
slotsWheel3Button = Button("slotsWheel3", 1110, 400, 100, 100, (100, 0, 155), (str(wheel3), (255, 255, 255), 1150, 425))

nimStartButton = Button("nimStart", 1170, 700, 400, 150, (0,0,255), ("Play Nim Type Zero", (255, 255, 255),1230, 725))


programPage = "Main Menu"
clickTimer = 0


run = True
while run == True:
    if clickTimer > 0:
        clickTimer -=1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    window.fill((155, 155, 155))
    mouseX, mouseY = pygame.mouse.get_pos()

    drawText(f"Bank Account: {bankAccount}", (255, 255, 255),1600, 25)
    
    
    for buttons in ButtonList:
        if buttons.x < mouseX < buttons.x + buttons.width and buttons.y < mouseY < buttons.y + buttons.height and buttons.inUse == True and pygame.mouse.get_pressed()[0]:
            if clickTimer <= 0:
                match buttons.name:
                    case "slotsRoll":
                        programPage, clickTimer, bankAccount, wheel1, wheel2, wheel3 = buttons.clicked(programPage, clickTimer, bankAccount)
                        slotsWheel1Button = Button("slotsWheel1", 710, 400, 100, 100, (100, 0, 155), (str(wheel1), (255, 255, 255), 750, 425))
                        slotsWheel2Button = Button("slotsWheel2", 910, 400, 100, 100, (100, 0, 155), (str(wheel2), (255, 255, 255), 950, 425))
                        slotsWheel3Button = Button("slotsWheel3", 1110, 400, 100, 100, (100, 0, 155), (str(wheel3), (255, 255, 255), 1150, 425))

                    case _: #basically the else of switch statements
                        programPage, clickTimer, bankAccount = buttons.clicked(programPage, clickTimer, bankAccount)
            else:
                programPage, clickTimer, bankAccount = buttons.clicked(programPage, clickTimer, bankAccount)
        buttons.draw()
        buttons.inUse = False

    if programPage != "Main Menu": #once u add blackjack and nim, add a game in progress variable and make this only show up when a game isnt in progress
        BackButton.inUse = True

    match programPage:

        case "Main Menu":
            BeginGamblingButton.inUse = True
            EnterAccountButton.inUse = True

        case "Login Menu":
            AccountLoginButton.inUse = True
            AccountRegisterButton.inUse = True

        case "Gambling Menu":
            blackjackStartButton.inUse = True
            slotsStartButton.inUse = True
            nimStartButton.inUse = True

        case "Blackjack":
            blackjackHitButton.inUse = True
            blackjackStandButton.inUse = True

        case "Slots":
            slotsRollButton.inUse = True
            slotsWheel1Button.inUse = True
            slotsWheel2Button.inUse = True
            slotsWheel3Button.inUse = True
            drawText("SLOTS", (255, 255, 255),910, 25)

    
    
    pygame.display.update()
    
    
pygame.quit()