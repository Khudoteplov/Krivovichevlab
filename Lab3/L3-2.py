import pygame
from pygame.draw import *
import numpy as np

pygame.init()
FPS = 30

width = 1400
height = 900

sc = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (154, 218, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
SKIN = (255, 223, 196)

sc.fill(LIGHT_BLUE)


def boy(x1, y1, x2, y2):  # x1, y1 - 1st hand, x2, y2 - 2nd hand
    x1, x2 = min(x1, x2), max(x1, x2)
    scale = (x2 - x1) / 240
    x = x1 + int(scale * 60)
    y = y1 - int(scale * 130)
    ellipse(sc, GRAY, (x, y, int(scale * 120), int(scale * 240)))  # body
    line(sc, BLACK, [int(scale * 20) + x, int(scale * 210) + y],
         [int(scale * -20) + x, int(scale * 360) + y])  # left leg
    line(sc, BLACK, [int(scale * -20) + x, int(scale * 360) + y],
         [int(scale * -50) + x, int(scale * 360) + y])  # left foot
    line(sc, BLACK, [int(scale * 99) + x, int(scale * 210) + y],
         [int(scale * 119) + x, int(scale * 360) + y])  # right leg
    line(sc, BLACK, [int(scale * 119) + x, int(scale * 360) + y],
         [int(scale * 149) + x, int(scale * 360) + y])  # right foot
    circle(sc, SKIN, (int(scale * 60) + x, int(scale * (-30)) + y), int(scale * 50))  # head
    line(sc, BLACK, [int(scale * 20) + x, int(scale * 30) + y],
         [int(scale * -60) + x, int(scale * 130) + y])  # left arm
    line(sc, BLACK, (int(scale * 100) + x, int(scale * 30) + y), [x2, y2])  # right arm


def icecream(x, y, angle=0.0, scale=1.0):
    a = int(scale * 80)
    polygon(sc, YELLOW, [[x, y],
                         [x + int(a * np.sin(np.pi / 8 + angle)),
                          y - int(a * np.cos(np.pi / 8 + angle))],
                         [x + int(a * np.sin(-np.pi / 8 + angle)),
                          y - int(a * np.cos(-np.pi / 8 + angle))],
                         [x, y]])
    circle(sc, (255, 0, 0), (x + int(1.1 * a * np.sin(-3.14 / 18 + angle)),
                             y - int(1.1 * a * np.cos(-3.14 / 18 + angle))), int(scale * 19))
    circle(sc, (85, 0, 0), (x + int(1.1 * a * np.sin(np.pi / 18 + angle)),
                            y - int(1.1 * a * np.cos(np.pi / 18 + angle))), int(scale * 19))
    circle(sc, WHITE, (x + int(1.4 * a * np.sin(angle)),
                       y - int(1.4 * a * np.cos(angle))), int(scale * 19))


def girl(x1, y1, x2, y2):  # x1, y1 - 1st hand, x2, y2 - 2nd (bent) hand
    scale = (x2 - x1) / 240
    x = x1 + int(scale * 60)
    y = y1 - abs(int(scale * 530))
    polygon(sc, PINK, [[int(scale * 60) + x, abs(int(scale * 320)) + y],
                       [int(scale * 120) + x, abs(int(scale * 630)) + y],
                       [int(scale * 0) + x, abs(int(scale * 630)) + y],
                       [int(scale * 60) + x, abs(int(scale * 320)) + y]])  # body
    circle(sc, SKIN, (int(scale * 60) + x, abs(int(scale * 370)) + y), abs(int(scale * 50)))  # head
    line(sc, BLACK, [int(scale * 30) + x, y + abs(int(scale * 630))],
         [int(scale * 30) + x, abs(int(scale * 750)) + y])  # 1st leg
    line(sc, BLACK, [int(scale * 30) + x, abs(int(scale * 750)) + y],
         [int(scale * 5) + x, abs(int(scale * 750)) + y])  # 1st foot
    line(sc, BLACK, [int(scale * 90) + x, y + abs(int(scale * 630))],
         [int(scale * 90) + x, abs(int(scale * 750)) + y])  # 2nd leg
    line(sc, BLACK, [int(scale * 90) + x, abs(int(scale * 750)) + y],
         [int(scale * 115) + x, abs(int(scale * 753)) + y])  # 2nd foot
    line(sc, BLACK, [int(scale * 40) + x, abs(int(scale * 430)) + y],
         [int(scale * -60) + x, abs(int(scale * 530)) + y])  # 1st (straight) arm
    line(sc, BLACK, [x2, y2], [int(scale * 125) + x, y1 - abs(int(scale * 30))])  # forearm
    line(sc, BLACK, [int(scale * 125) + x, y1 - abs(int(scale * 30))],
         [int(scale * 80) + x, abs(int(scale * 430)) + y])  # upper arm


def ball(x, y, angle=1.0, scale=1.0):
    a = int(scale * 120)
    line(sc, BLACK, [x, y], [int(a * np.sin(angle)) + x, -int(a * np.cos(angle)) + y])
    polygon(sc, RED, [[int(a * np.sin(angle)) + x, -int(a * np.cos(angle)) + y],
                      [int(a * np.sin(angle) + 0.6 * a * np.sin(angle + 3.14 / 5)) + x,
                       -int(a * np.cos(angle) + 0.6 * a * np.cos(angle + 3.14 / 5)) + y],
                      [int(a * np.sin(angle) + 0.6 * a * np.sin(angle - 3.14 / 5)) + x,
                       -int(a * np.cos(angle) + 0.6 * a * np.cos(angle - 3.14 / 5)) + y],
                      [int(a * np.sin(angle)) + x, -int(a * np.cos(angle)) + y]])
    circle(sc, RED, (int(a * np.sin(angle) + 0.6 * a * np.sin(angle + 3.14 / 10)) + x,
                     -int(a * np.cos(angle) + 0.6 * a * np.cos(angle + 3.14 / 10)) + y), int(a / 5.2))
    circle(sc, RED, (int(a * np.sin(angle) + 0.6 * a * np.sin(angle - 3.14 / 10)) + x,
                     -int(a * np.cos(angle) + 0.6 * a * np.cos(angle - 3.14 / 10)) + y), int(a / 5.2))
    circle(sc, RED, (int(a * np.sin(angle) + 0.55 * a * np.sin(angle)) + x,
                     -int(a * np.cos(angle) + 0.55 * a * np.cos(angle)) + y), int(a / 12))


horizon = 400

rect(sc, GREEN, (0, horizon, width, height - horizon))

boy(0, 450, 70, 450)
girl(70, 450, 150, 460)
boy(150, 460, 300, 480)
icecream(540, 500, 0.9, 0.3)
ball(300, 480, 0.0, 1.0)
girl(500, 500, 300, 480)
boy(500, 500, 540, 500)
girl(600, 500, 700, 500)
ball(600, 500, -0.2, 0.6)
icecream(700, 500, 0.1, 1.1)
boy(900, 450, 1200, 450)
ball(1200, 450, -0.2, 2.0)
icecream(900, 450, 0.2, 0.9)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
