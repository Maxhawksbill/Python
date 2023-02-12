import random
# from random import randint
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
from os import listdir

pygame.init()
FPS = pygame.time.Clock()

screen = width, height = 800, 600
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 255, 0
main_screen = pygame.display.set_mode(screen)
IMG_PATH = 'E:\Python\Python\Ball\Goose'
bg = pygame.transform.scale(pygame.image.load('E:\Python\Python\Ball\Background.png').convert(), screen)
bg_x = 0
bg_x2 = bg.get_width()
bg_speed = 3

player_img = [pygame.image.load(IMG_PATH + '/' + file).convert_alpha() for file in listdir(IMG_PATH)]
player = player_img[4]
player_rect = player.get_rect()
player_speed = 10

font = pygame.font.SysFont('verdana', 20, bold=True)

enemy_x = 120
enemy_y = 20


def create_enemy():
    enemy = pygame.transform.scale(pygame.image.load('E:\Python\Python\Ball\enemy.png').convert_alpha(),
                                   (enemy_x, enemy_y))
    enemy_rect = pygame.Rect(width, random.randint(enemy_y, height - enemy_y), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
enemies = []

bonus_x = 70
bonus_y = 100


def create_bonuses():
    bonus = pygame.transform.scale(pygame.image.load('E:\Python\Python\Ball\Bonus.png').convert_alpha(),
                                   (bonus_x, bonus_y))
    bonus_rect = pygame.Rect(random.randint(bonus_x, width - bonus_x), 0, *bonus.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus, bonus_rect, bonus_speed]

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 3500)
bonuses = []

CHANGE_IMG = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMG, 125)
img_index = 0

scores = 0

is_working = True

while is_working:
    FPS.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonuses())
        if event.type == CHANGE_IMG:
            img_index += 1
            if img_index == len(player_img):
                img_index = 0
            player = player_img[img_index]

    precised_keys = pygame.key.get_pressed()

    bg_x -= bg_speed
    bg_x2 -= bg_speed
    if bg_x < -bg.get_width():
        bg_x = bg.get_width()
    if bg_x2 < -bg.get_width():
        bg_x2 = bg.get_width()

    main_screen.blit(bg, (bg_x, 0))
    main_screen.blit(bg, (bg_x2, 0))

    main_screen.blit(player, player_rect)
    main_screen.blit(font.render(str(scores), True, GREEN), (width - 30, 0))

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_screen.blit(enemy[0], enemy[1])
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        if player_rect.colliderect(enemy[1]):
            is_working = False
        # print(len(enemies))

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_screen.blit(bonus[0], bonus[1])

        if bonus[1].bottom > height:
            bonuses.pop(bonuses.index(bonus))
        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1

    if precised_keys[K_DOWN] and player_rect.bottom <= height:
        player_rect = player_rect.move(0, player_speed)
    if precised_keys[K_UP] and player_rect.top >= 0:
        player_rect = player_rect.move(0, -player_speed)
    if precised_keys[K_RIGHT] and player_rect.right <= width:
        player_rect = player_rect.move(player_speed, 0)
    if precised_keys[K_LEFT] and player_rect.left >= 0:
        player_rect = player_rect.move(-player_speed, 0)

    pygame.display.flip()
