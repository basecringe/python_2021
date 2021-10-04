import pygame
from pygame.draw import *

pygame.init()

FPS = 30


white = (230, 230, 230)
fiol = (128, 0, 128)
blue = (121, 121, 242)
black = (0, 0, 0)
green = (22, 80, 68)
gray = (77, 77, 77)
fish = (191, 203, 200)
red = (221, 166, 166)
blood = (211, 18, 23)
screen = pygame.display.set_mode((600, 800))
screen.fill(white)

line(screen, black, (0, 400), (600, 400), 4)
rect(screen, fiol, (0, 0, 600, 400))

circle(screen, blood, (350, 100), 100, 7)
polygon(screen, blood, [(290, 30), (350, 200), (410, 30),(260, 130), (440, 130), (290, 30)], 7)

ellipse(screen, gray, (350, 550, 200, 80))
ellipse(screen, black, (350, 550, 200, 80), 2)
ellipse(screen, green, (370, 580, 160, 50))
ellipse(screen, black, (370, 580, 160, 50), 2)

arc(screen, black, [220, 180, 800, 600], 2, 3, 4)
line(screen, black, (450, 210), (450, 600), 2)

ellipse(screen, white, (95, 245, 140, 75))
ellipse(screen, black, (95, 245, 140, 75), 2)
ellipse(screen, white, (10, 300, 190, 350))
ellipse(screen, black, (10, 300, 190, 350), 2)
ellipse(screen, white, (95, 550, 160, 120))
ellipse(screen, black, (95, 550, 160, 120), 2)
ellipse(screen, white, (170, 650, 110, 45))
ellipse(screen, black, (170, 650, 110, 45), 2)
ellipse(screen, white, (170, 370, 90, 45))
ellipse(screen, black, (170, 370, 90, 45), 2)
circle(screen, white, (117, 255), 12)
circle(screen, black, (117, 255), 12, 2)
ellipse(screen, black, (155, 265, 9, 7))
ellipse(screen, black, (230, 275, 9, 7))
arc(screen, black, [90, 280, 140, 20], -1.57, 0, 1)


transparent = (0, 0, 0, 0)
tail = pygame.Surface((160, 140))
tail = tail.convert_alpha()
tail.fill(transparent)
polygon(tail, red, [(100,25), (90,5), (120, 10), (122, 12), (120,20), (100, 25)])
polygon(tail, black, [(100,25), (90,5), (120, 10), (122, 12), (120,20), (100, 25)], 2)
polygon(tail, red, [(70,55), (83,55), (85, 68), (65, 70), (69, 60), (70, 55)])
polygon(tail, black, [(70,55), (83,55), (85, 68), (65, 70), (69, 60), (70, 55)], 2)
polygon(tail, red, [(110,55), (120,55), (125, 60), (130, 68), (115, 75), (110, 55)])
polygon(tail, black, [(110,55), (120,55), (125, 60), (130, 68), (115, 75), (110, 55)], 2)
ellipse(tail, fish, (40, 20, 120, 40))
ellipse(tail, black, (40, 20, 120, 40), 2)
polygon(tail, fish, [(5,15), (5,65), (40, 40), (5,15)])
polygon(tail, black, [(5,15), (5, 65), (40, 40), (5,15)], 2)
circle(tail, blue, (130, 40), 7)
circle(tail, black, (131, 41), 4)
tail = pygame.transform.rotate(tail, 30)
pygame.Surface.blit(screen, tail, (370, 630))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
