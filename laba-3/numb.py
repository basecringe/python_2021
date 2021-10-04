import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400))

circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (0, 0, 0), (200, 175), 100, 2)

circle(screen, (255, 0, 0), (230, 155), 15)
circle(screen, (0, 0, 0), (230, 155), 15, 2)
circle(screen, (0, 0, 0), (230, 155), 7)

circle(screen, (255, 0, 0), (165, 155), 20)
circle(screen, (0, 0, 0), (165, 155), 20, 2)
circle(screen, (0, 0, 0), (165, 155), 7)

rect(screen, (0, 0, 0), (160, 220, 80, 20))

polygon(screen, (0, 0, 0), [(100,85), (190,140),
                               (185,150), (95,95), (100,85)])
polygon(screen, (0, 0, 0), [(300,100), (210,140),
                               (215,150), (305,110), (300,100)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
