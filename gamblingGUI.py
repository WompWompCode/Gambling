#######################################
#THIS ENTIRE FILE IS A WORK IN PROGRESS
#######################################

from random import randint
import pygame
pygame.init()
window = pygame.display.set_mode([1920, 1080])

textFont = pygame.font.SysFont("Arial", 30)

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
            
    def clicked(self, programPage, clickTimer):
        if clickTimer <= 0:
            match self.name:

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
                    print(wheel1, wheel2, wheel3)
                    return programPage, 60, wheel1, wheel2, wheel3

                case "nimStart":
                    programPage = "Nim"
        

        
        return programPage, 60

ButtonList = []
textFont = pygame.font.SysFont("Arial", 40)
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
    
    
    for buttons in ButtonList:
        if buttons.x < mouseX < buttons.x + buttons.width and buttons.y < mouseY < buttons.y + buttons.height and buttons.inUse == True and pygame.mouse.get_pressed()[0]:
            if clickTimer <= 0:
                match buttons.name:
                    case "slotsRoll":
                        programPage, clickTimer, wheel1, wheel2, wheel3 = buttons.clicked(programPage, clickTimer)
                        slotsWheel1Button = Button("slotsWheel1", 710, 400, 100, 100, (100, 0, 155), (str(wheel1), (255, 255, 255), 750, 425))
                        slotsWheel2Button = Button("slotsWheel2", 910, 400, 100, 100, (100, 0, 155), (str(wheel2), (255, 255, 255), 950, 425))
                        slotsWheel3Button = Button("slotsWheel3", 1110, 400, 100, 100, (100, 0, 155), (str(wheel3), (255, 255, 255), 1150, 425))

                    case _: #basically the else of switch statements
                        programPage, clickTimer = buttons.clicked(programPage, clickTimer)
            else:
                programPage, clickTimer = buttons.clicked(programPage, clickTimer)
        buttons.draw()
        buttons.inUse = False

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

    
    
    pygame.display.update()
    
    
pygame.quit()