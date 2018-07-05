#Justin Hendrick http://code.google.com/p/colorful-snake
import pygame
import os
from random import randint

# draw menu selection box
def menusel(select, col):
    if select == 0:
        draw(9, 11, 30, col)
    if select == 1:
        draw(9, 13, 30, col)
    if select == 2:
        draw(9, 15, 30, col)
    if select == 3:
        draw(9, 17, 30, col)
    if select == 4:
        draw(9, 19, 30, col)

#draws rounded squares
def draw(x, y, sz, col):
    clock.tick(55)
    x *= sz
    y *= sz
    if col == "sn":
        r = randint(100,200)
        g = randint(100,200)
        b = randint(100,200)
    if col == "bl":
        r = g = b = 0
    rad=(sz - 2) / 2
    l=range(-rad, rad + 1)
    for ix in l:
        for iy in l:
            if (ix == -rad or ix == rad) and (iy == -rad or iy == rad):
                pass
            else:
                screen.set_at((x + ix, y + iy), (r, g, b))
    pygame.display.flip()

#set screen and clock
pygame.init()
screen = pygame.display.set_mode((770,700))
pygame.display.set_caption("Colorful Snake by Justin Hendrick")
clock = pygame.time.Clock()

#draw snake logo
draw(11, 6, 15, "sn")
for i in range(5, 16):
    draw(41, i, 15, "sn")
for i in range(42, 45):
    draw(i, 10, 15, "sn")
for i in range(5, 12):
    draw(i, 10, 15, "sn")
for i in range(10, 15):
    draw(11, i, 15, "sn")
for i in range(11, 4, -1):
    draw(i, 15, 15, "sn")
draw(5, 14, 15, "sn")
draw(15, 6, 15, "sn")
draw(17, 9, 15, "sn")
draw(17, 10, 15, "sn")
for i in range(15, 4, -1):
    draw(14, i, 15, "sn")
draw(14, 5, 15, "sn")
draw(18, 11, 15, "sn")
draw(15, 6, 15, "sn")
draw(16, 7, 15, "sn")
for i in range(5, 12):
    draw(i, 5, 15, "sn")
draw(16, 8, 15, "sn")
draw(18, 12, 15, "sn")
for i in range(42, 46):
    draw(i, 5, 15, "sn")
    draw(i, 15, 15, "sn")
for i in range(25, 29):
    draw(i, 5, 15, "sn")
for i in range(25, 29):
    draw(i, 9, 15, "sn")
draw(19, 13, 15, "sn")
for i in range(15, 4, -1):
    draw(24, i, 15, "sn")
for i in range(6, 10):
    draw(5, i, 15, "sn")
x = 33
y = 10
b = 10
for i in range(6):
    draw(x, y, 15, "sn")
    draw(x, b, 15, "sn")
    x += 1
    y -= 1
    b += 1
for i in range(15, 4, -1):
    draw(29, i, 15, "sn")
for i in range(5, 16):
    draw(32, i, 15, "sn")
draw(19, 14, 15, "sn")
draw(20,15,15,"sn")
for i in range(15, 4, -1):
    draw(21, i, 15, "sn")

#write choices onto screen
arial = pygame.font.SysFont("arial", 30)
ez = arial.render("Easy", True, (255, 255, 255))
md = arial.render("Medium", True, (255, 255, 255))
hd = arial.render("Hard", True, (255, 255, 255))
hs = arial.render("High Scores", True, (255, 255, 255))
qt = arial.render("Quit", True, (255, 255, 255))
screen.blit(ez, (310, 315))
screen.blit(md, (310, 375))
screen.blit(hd, (310, 435))
screen.blit(hs, (310, 495))
screen.blit(qt, (310, 555))
pygame.display.flip()

#setup menu loop
menu = True
select = 0
menusel(select, "sn")

#mnu loop
while menu:
    #slow it down to 25 fps and enable x to close
    clock.tick(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        elif event.type == pygame.KEYDOWN:

            #menu movement
            if event.key == pygame.K_UP:
                    menusel(select, "bl")
                    select -= 1
                    if select == -1:
                        select = 4
                    menusel(select, "sn")
            if event.key == pygame.K_DOWN:
                    menusel(select, "bl")
                    select += 1
                    if select == 5:
                        select = 0
                    menusel(select, "sn")

            #menu selection
            if event.key == pygame.K_RETURN:
                    if select == 0: #play on easy
                        trans = open(".dif.txt", "w")
                        trans.write("Easy")
                        trans.close()
                        execfile("colorfulsnake_4.py")
                        execfile("menu.py")

                    if select == 1: #play on medium
                        trans = open(".dif.txt", "w")
                        trans.write("Medium")
                        trans.close()
                        execfile("colorfulsnake_4.py")
                        execfile("menu.py")

                    if select == 2: #play on hard
                        trans = open(".dif.txt", "w")
                        trans.write("Hard")
                        trans.close()
                        execfile("colorfulsnake_4.py")
                        execfile("menu.py")

                    if select == 3: #show highscore
                        if os.path.exists(".sn_hiscore.txt") == False:
                            hsf = open(".sn_hiscore.txt","w")
                            hsf.write("0\n0\n0")
                            hsf.close()
                        hsfa = open(".sn_hiscore.txt", "r")
                        chs = hsfa.read()
                        hsfa.close()
                        chs = chs.split("\n")
                        screen = pygame.display.set_mode((770, 700))
                        for i in range(0, 3):
                            chs[i] = eval(chs[i])
                        highe = arial.render("Easy:       %d" %chs[0], True, (255, 255, 255))
                        highm = arial.render("Medium:   %d" %chs[1], True, (255, 255, 255))
                        highh = arial.render("Hard:       %d" %chs[2], True, (255, 255, 255))
                        kcont = arial.render("Press any key to continue", True, (255, 255, 255))
                        screen.blit(highe, (310, 170))
                        screen.blit(highm, (310, 320))
                        screen.blit(highh, (310, 470))
                        screen.blit(kcont, (240, 590))
                        pygame.display.flip()
                        while pygame.event.wait().type != pygame.KEYDOWN and pygame.event.wait().type != pygame.QUIT:
                            pass
                        execfile("menu.py")
                    if select == 4: #quit
                        menu = False
