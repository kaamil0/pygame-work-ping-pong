import pygame
import random

pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

player = pygame.Rect(250, 550, 100, 20)
player_speed = 7

enemy = pygame.Rect(random.randint(0, 550), 0, 50, 50)
enemy_speed = 5

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < width - player.width:
        player.x += player_speed

    enemy.y += enemy_speed

    if enemy.y > height:
        enemy.y = 0
        enemy.x = random.randint(0, 550)

    if player.colliderect(enemy):
        enemy.y = 0
        enemy.x = random.randint(0, 550)

    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.update()

pygame.quit()
