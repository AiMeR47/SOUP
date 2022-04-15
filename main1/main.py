import pygame, sys, os, random
from pygame import mixer
from button import Button

WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT), -40,-40)
pygame.display.set_caption("SOUP")
FPS = 60
trash = []
def image ():
    BG = pygame.image.load("assets/bg.png")
    global BG3
    BG3 = pygame.image.load("assets/bg3.png")
    cloud = pygame.image.load("assets/cload.png")
    cloud2 = pygame.image.load("assets/cload2.png")
    BG_2 = pygame.image.load("assets/bg-2.png")
    global cloud_2
    global cloud2_2
    global paper
    cloud_2 = pygame.image.load("assets/cloud4.png")
    cloud2_2 = pygame.image.load("assets/cloud5.png")
    global tree
    tree = pygame.image.load("assets/tree1.png")
    global tree2
    tree2 = pygame.image.load("assets/tree2.png")
    can = pygame.image.load("assets/can.png")
    garbage = pygame.image.load("assets/garbage_bag.png")
    banana = pygame.image.load("assets/banana_peel.png")
    paper = pygame.image.load("assets/papers.png")
    dog1 = pygame.image.load("assets/dog1.png")
    global animal1
    global animal2
    global animal3
    global bg2_2
    animal1 = pygame.image.load("assets/animal1.png")
    animal2 = pygame.image.load("assets/animal2.png")
    animal3 = pygame.image.load("assets/animal3.png")
    global ozon1
    global ozon2
    global ozon3
    global ozon4
    dog11 = pygame.transform.scale(dog1, (200, 150))
    dog2 = pygame.image.load("assets/dog2.png")
    dog22 = pygame.transform.scale(dog2, (200, 150))
    dog3 = pygame.image.load("assets/dog3.png")
    dog33 = pygame.transform.scale(dog3, (200, 150))
    dog4 = pygame.image.load("assets/dog4.png")
    dog44 = pygame.transform.scale(dog4, (200, 150))
    dog5 = pygame.image.load("assets/dog5.png")
    dog55 = pygame.transform.scale(dog5, (200, 150))
    dog6 = pygame.image.load("assets/dog6.png")
    dog66 = pygame.transform.scale(dog6, (200, 150))
    dog7 = pygame.image.load("assets/dog7.png")
    dog77 = pygame.transform.scale(dog7, (200, 150))
    dog8 = pygame.image.load("assets/dog8.png")
    dog88 = pygame.transform.scale(dog8, (200, 150))
    global garbage1
    global banana1
    global can1
    global paper1
    global bg3
    bg3 = pygame.transform.scale(BG3, (1280, 720))
    tree = pygame.transform.scale(tree, (400, 400))
    tree2 = pygame.transform.scale(tree2, (400, 400))
    garbage1 = pygame.transform.scale(garbage, (50, 50))
    banana1 = pygame.transform.scale(banana, (50, 50))
    can1 = pygame.transform.scale(can, (25, 50))
    paper1 = pygame.transform.scale(paper, (50, 50))
    animal1 = pygame.transform.scale(animal1, (50, 50))
    animal2 = pygame.transform.scale(animal2, (50, 50))
    animal3 = pygame.transform.scale(animal3, (50, 50))
    global dog
    global left
    global left2
    dog =  [dog11, dog22, dog33, dog44, dog55, dog66, dog77, dog88]
    left =  [pygame.image.load(os.path.join("assets/", "aish1.png")),
             pygame.image.load(os.path.join("assets/", "aish2.png")),
             pygame.image.load(os.path.join("assets/", "aish3.png")),
             pygame.image.load(os.path.join("assets/", "aish4.png")),
             pygame.image.load(os.path.join("assets/", "aish5.png")),
             pygame.image.load(os.path.join("assets/", "aish6.png")),]
    left2 =  [pygame.image.load(os.path.join("assets/", "ganav1.png")),
              pygame.image.load(os.path.join("assets/", "ganav2.png")),
              pygame.image.load(os.path.join("assets/", "ganav3.png")),
              pygame.image.load(os.path.join("assets/", "ganav4.png")),
              pygame.image.load(os.path.join("assets/", "ganav5.png")),
              pygame.image.load(os.path.join("assets/", "ganav6.png")),]
    global bg2
    global  ozon
    global animals
    bg2 = pygame.transform.scale(BG, (1280, 720))
    bg2_2 = pygame.transform.scale(BG_2, (1280, 720))
    global cloud23
    global cloud24
    cloud23 = pygame.transform.scale(cloud2, (300, 300))
    cloud24 = pygame.transform.scale(cloud2, (300, 300))
    global cloud60
    global cloud70
    cloud60 = pygame.transform.scale(cloud_2, (300, 300))
    cloud70 = pygame.transform.scale(cloud2_2, (300, 300))
    global  cloud_x
    global cloud_x2
    cloud_x = 1300
    cloud_x2 = 10000
    global stepIndex
    global  cloud_count
    stepIndex = 0
    cloud_count = 0
def draw_win():
    garbage = pygame.image.load("assets/garbage_bag.png")
    banana = pygame.image.load("assets/banana_peel.png")
    paper = pygame.image.load("assets/papers.png")
    dog1 = pygame.image.load("assets/dog1.png")
    trash = [garbage1, paper1, banana1, can1, ]
    WIN.blit(bg2, (0,0))
    WIN.blit(tree, (cloud_x + 100, 278))
    WIN.blit(cloud23, (cloud_x, 20))
    WIN.blit(cloud24, (cloud_x2, 160))
    global stepIndex
    if stepIndex >=6:
        stepIndex = 0
    WIN.blit(left[int(stepIndex)], (boysx, 250))
    if stepIndex >=6:
        stepIndex = 0
    WIN.blit(left2[int(stepIndex)], (1000, 250))
    WIN.blit(trash[stepIndex2], (trash_x, 510))
    WIN.blit(dog[int(stepIndex)], (dog_x, 400))
    pygame.display.update()
    stepIndex += 0.3



pygame.init()
menuBG2 = pygame.image.load("assets/Background.png")
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")



def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        image()
        global stepIndex2
        stepIndex2 = 0
        global count1
        count1 = 0
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        global dog_x
        dog_x = 100
        global vel
        vel = 30
        global trash_x
        trash_x = 1200
        global boysx
        boysx = 600
        clock = pygame.time.Clock()
        run = True
        global cloud_x
        global cloud_x2
        global cloud_count
        while run:
            cloud_x -= 2.3
            cloud_x2 -= 1.5
            random12 = random.randint(0, 20)
            count1 += 1
            if count1 >= 20:
                count1 = 0
            clock.tick(FPS)
            if boysx <= dog_x:
                Game_Over()
            if trash_x > dog_x + 50:
                trash_x -= vel
            else:
                trash_x = 10500
                stepIndex2 = random.randint(0, 3)
                boysx -= 100
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and boysx + 208 >= trash_x and boysx + 35 <= trash_x:
                    if event.key == pygame.K_SPACE:
                        trash_x = 10500
                        if boysx <= 800:
                            boysx += 100
                        else:
                            you_won()
            if cloud_x < dog_x -400:
                cloud_x = 1300
            if random12 == count1 and trash_x <= 10500 and trash_x > 1200:
                trash_x = 1200
                if (cloud_x2 <=11000 and cloud_x2 >= 2000) or cloud_x2 <= dog_x -320:
                    cloud_x2 = 1300
            draw_win()
        pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()

def draw_win_2():
    trash2 = [paper1, garbage1, banana1, can1]
    animals = [animal1, animal2, animal3]
    WIN.blit(bg2_2, (0,0))
    WIN.blit(tree2, (cloud_x + 100, 278))
    WIN.blit(cloud_2, (cloud_x, 20))
    WIN.blit(cloud2_2, (cloud_x2, 160))
    global stepIndex
    if stepIndex >=6:
        stepIndex = 0
    WIN.blit(left[int(stepIndex)], (boysx, 250))
    if stepIndex >=6:
        stepIndex = 0
    WIN.blit(left2[int(stepIndex)], (1000, 250))
    WIN.blit(trash2[stepIndex2], (trash_x, 510))
    WIN.blit(animals[stepIndex3], (animal_x, 510))
    WIN.blit(dog[int(stepIndex)], (dog_x, 400))
    pygame.display.update()
    stepIndex += 0.3



def play_2():
    while True:
        image()
        global stepIndex2
        stepIndex2 = 0
        global stepIndex3
        stepIndex3 = 0
        global count1
        count1 = 0
        global dog_x
        dog_x = 100
        global vel
        vel = 30
        global trash_x
        trash_x = 1200
        global animal_x
        animal_x = 1200
        global boysx
        boysx = 600
        clock = pygame.time.Clock()
        run = True
        global cloud_x
        global cloud_x2
        global cloud_count
        global  count2
        count2 = 0
        while run:
            cloud_x -= 2.3
            cloud_x2 -= 1.5
            random12 = random.randint(0, 20)
            random22 = random.randint(0, 20)
            count1 += 1
            count2 += 1
            if count1 >= 20:
                count1 = 0
            if count2 >= 20:
                count2 = 0
            clock.tick(FPS)
            if boysx <= dog_x:
                Game_Over()
            if trash_x > dog_x + 50:
                trash_x -= vel
            else:
                trash_x = 10500
                stepIndex2 = random.randint(0, 3)
                boysx -= 100
            if animal_x > dog_x + 50:
                animal_x -= vel
            else:
                animal_x = 10500
                stepIndex3 = random.randint(0, 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and boysx + 208 >= trash_x and boysx + 35 <= trash_x:
                    if event.key == pygame.K_SPACE:
                        trash_x = 10500
                        if boysx <= 800:
                            boysx += 100
                        else:
                            you_won_1()
                if event.type == pygame.KEYDOWN and boysx + 208 >= animal_x and boysx + 35 <= animal_x:
                    if event.key == pygame.K_SPACE:
                        animal_x = 10500
                        boysx -= 100
            if cloud_x < dog_x -600:
                cloud_x = 1300
            if random12 == count1 and trash_x <= 10500 and trash_x > 1200:
                trash_x = 1200
            if random22 == count2 and animal_x <= 10500 and animal_x > 1200:
                animal_x = 1200
                if (cloud_x2 <=11000 and cloud_x2 >= 2000) or cloud_x2 <= dog_x -320:
                    cloud_x2 = 1300
            if trash_x == animal_x or trash_x + 1 == animal_x or trash_x + 2 == animal_x or trash_x + 3 == animal_x or trash_x + 4 == animal_x or trash_x + 5 == animal_x or  trash_x + 6 == animal_x or animal_x +1 == trash_x or animal_x +2 == trash_x or animal_x +3 == trash_x or animal_x +3 == trash_x or animal_x +5 == trash_x or animal_x +6 == trash_x:
                trash_x = 1200
            draw_win_2()
        pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()

def draw_win_3():
    trash2 = [paper1, garbage1, banana1, can1]
    animals = [animal1, animal2, animal3]
    WIN.blit(bg3, (0, 0))
    almog = pygame.image.load("assets/almog1.png")
    almog2 = pygame.image.load("assets/almog2.png")
    almog = pygame.transform.scale(almog, (250, 250))
    almog2 = pygame.transform.scale(almog2, (250, 250))
    ozon1 = pygame.image.load("assets/ozon1.png")
    ozon2 = pygame.image.load("assets/ozon3.png")
    ozon3 = pygame.image.load("assets/ozon4.png")
    ozon4 = pygame.image.load("assets/ozon5.png")
    ozon1 = pygame.transform.scale(ozon1, (600, 600))
    ozon2 = pygame.transform.scale(ozon2, (600, 600))
    ozon3 = pygame.transform.scale(ozon3, (600, 600))
    ozon4 = pygame.transform.scale(ozon4, (600, 600))
    ozon = [ozon1,ozon2,ozon3,ozon4]
    WIN.blit(ozon[int(stepIndex4)], (0,-50))
    WIN.blit(almog, (almog_x, 374))
    WIN.blit(almog2, (almog_x +300, 405))
    WIN.blit(cloud_2, (cloud_x, 20))
    WIN.blit(cloud2_2, (cloud_x2, 160))
    global stepIndex
    if stepIndex >=6:
        stepIndex = 0
    WIN.blit(left[int(stepIndex)], (boysx, 250))
    if stepIndex >=6:
        stepIndex = 0
    WIN.blit(left2[int(stepIndex)], (1000, 250))
    WIN.blit(trash2[stepIndex2], (trash_x, 510))
    WIN.blit(animals[stepIndex3], (animal_x, 510))
    WIN.blit(dog[int(stepIndex)], (dog_x, 400))
    pygame.display.update()
    stepIndex += 0.3

def play_3():
    while True:
        image()
        global almog_x
        almog_x=1400
        global stepIndex2
        stepIndex2 = 0
        global stepIndex3
        stepIndex3 = 0
        global stepIndex4
        stepIndex4 = 0
        global count1
        count1 = 0
        global dog_x
        dog_x = 100
        global vel
        vel = 30
        global trash_x
        trash_x = 1200
        global animal_x
        animal_x = 1200
        global boysx
        boysx = 600
        clock = pygame.time.Clock()
        run = True
        global cloud_x
        global cloud_x2
        global cloud_count
        global  count2
        count2 = 0
        while run:
            almog_x -= 8
            if almog_x < dog_x -850:
                almog_x =1400
            random12 = random.randint(0, 20)
            random22 = random.randint(0, 20)
            count1 += 1
            count2 += 1
            if count1 >= 20:
                count1 = 0
            if count2 >= 20:
                count2 = 0
            if stepIndex4 !=3:
                stepIndex4 += 0.1
            if stepIndex4 >= 3:
                stepIndex4 = 3
            clock.tick(FPS)
            if boysx <= dog_x:
                Game_Over()
            if trash_x > dog_x + 50:
                trash_x -= vel +22
            else:
                trash_x = 10500
                stepIndex2 = random.randint(0, 3)
                boysx -= 100
            if animal_x > dog_x + 50:
                animal_x -= vel +22
            else:
                animal_x = 10500
                stepIndex3 = random.randint(0, 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and boysx + 208 >= trash_x and boysx + 35 <= trash_x:
                    if event.key == pygame.K_SPACE:
                        trash_x = 10500
                        if boysx <= 800:
                            boysx += 100
                        else:
                            you_won()
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                             boysx -=100
                if event.type == pygame.KEYDOWN and boysx + 208 >= animal_x and boysx + 35 <= animal_x:
                    if event.key == pygame.K_SPACE:
                        animal_x = 10500
                        boysx -= 100
            if cloud_x < dog_x -400:
                cloud_x = 1300
            if random12 == count1 and trash_x <= 10500 and trash_x > 1200:
                trash_x = 1200
            if random22 == count2 and animal_x <= 10500 and animal_x > 1200:
                animal_x = 1200
                if (cloud_x2 <=11000 and cloud_x2 >= 2000) or cloud_x2 <= dog_x -320:
                    cloud_x2 = 1300
            if trash_x == animal_x or trash_x + 1 == animal_x or trash_x + 2 == animal_x or trash_x + 3 == animal_x or trash_x + 4 == animal_x or trash_x + 5 == animal_x or  trash_x + 6 == animal_x or animal_x +1 == trash_x or animal_x +2 == trash_x or animal_x +3 == trash_x or animal_x +3 == trash_x or animal_x +5 == trash_x or animal_x +6 == trash_x:
                trash_x = 1200
            draw_win_3()
        pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()


pygame.mixer.music.load("assets/menu.mp3")
mixer.music.play(-1)
def main_menu():
    while True:
        SCREEN.blit(menuBG2, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("SOUP", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 480),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    mixer.music.play(0)
                    pygame.mixer.music.load("assets/level1.mp3")
                    mixer.music.play(-1)
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def you_won():
    while True:
        SCREEN.blit(menuBG2, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("You Won!", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/playagain.png"), pos=(640, 350),
                             text_input="PlayAgain", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        Level_BUTTON = Button(image=pygame.image.load("assets/playagain.png"), pos=(640, 480),
                             text_input="Next Level", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 610),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON,Level_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if Level_BUTTON.checkForInput(MENU_MOUSE_POS):
                    mixer.music.play(0)
                    pygame.mixer.music.load("assets/level2.mp3")
                    mixer.music.play(-1)
                    play_2()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def you_won_1():
    while True:
        SCREEN.blit(menuBG2, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("You Won!", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/playagain.png"), pos=(640, 350),
                             text_input="PlayAgain", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        Level_BUTTON = Button(image=pygame.image.load("assets/playagain.png"), pos=(640, 480),
                             text_input="Next Level", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 610),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON,Level_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if Level_BUTTON.checkForInput(MENU_MOUSE_POS):
                    mixer.music.play(0)
                    pygame.mixer.music.load("assets/level3.mp3")
                    mixer.music.play(-1)
                    play_3()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def Game_Over():
    while True:
        SCREEN.blit(menuBG2, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("You Lose!", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/playagain.png"), pos=(640, 350),
                             text_input="PlayAgain", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 480),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
main_menu()