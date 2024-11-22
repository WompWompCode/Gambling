

#######################################
#THIS ENTIRE FILE IS A WORK IN PROGRESS
#######################################


import pygame
pygame.init()
window = pygame.display.set_mode([1920, 1080])

textFont = pygame.font.SysFont("Arial", 30)

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
        ButtonList.append(self)
        self.inUse = False
        self.text = text
        
        
    def draw(self):
        if self.inUse == True:
            pygame.draw.rect(window, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))
            if self.text != "none":
                drawText(self.text[0], self.text[1], self.text[2], self.text[3])
            
    def clicked(self):
        if self.name == "menuBeginGamblingButton":
            gamblingMenu()
        elif self.name == "gamblingStartButton":
            (" ")

ButtonList = []
menuBeginGamblingButton = Button("menuBeginGamblingButton", 760, 700, 400, 150, (255, 0 , 0), ("Start Gambling", (255, 255, 255),770, 720))
gamblingStartButton = Button("gamblingStartButton", 760, 700, 400, 150, (0,0,255), ("Play Blackjack", (255, 255, 255),770, 720))

def mainMenu():
    for buttons in ButtonList:
        buttons.inUse = False
    menuBeginGamblingButton.inUse = True
    
def gamblingMenu():
    for buttons in ButtonList:
        buttons.inUse = False
    gamblingStartButton.inUse = True





mainMenu()

run = True
while run == True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    window.fill((155, 155, 155))
    
    mouseX, mouseY = pygame.mouse.get_pos()
    
    
    for buttons in ButtonList:
        if buttons.x < mouseX < buttons.x + buttons.width and buttons.y < mouseY < buttons.y + buttons.height and buttons.inUse == True and pygame.mouse.get_pressed()[0]:
            buttons.clicked()
        buttons.draw()
    
    
    pygame.display.update()
    
    
pygame.quit()