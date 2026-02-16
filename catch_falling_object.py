import pygame

import random

pygame.init()

width = 800

height = 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("catch the falling object")

clock = pygame.time.Clock()
FPS = 60

player_x = 350
player_y = 500 
player_speed = 7

object_x = random.randint(0, width-50)
object_y = 0
object_speed = 2
object_size = 10

score = 0
font = pygame.font.Font(None, 36)

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
    
    
    
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    player_x = max(0,min(player_x,width -50))

    object_y += object_speed

    if object_y > player_y and player_x <object_x +object_size and player_x + 50 > object_x:

        score += 1
        object_y = 0
        object_x = random.randint(0, width - 50)
        object_speed += 0.1

    if object_y > height:
        object_y = 0
        object_x = random.randint(0, width - 50)
        object_speed = 1.5

    screen.fill()
    pygame.draw.rect(screen,(255,255,255),(player_x,player_y,50,20))
    pygame.draw.rect(screen, (255,0,0), (object_x, object_y, object_size, object_size))
    
    score_text = font.render(f"Score: {score}", True (255,255,255))
    screen.blit(score_text(10,10))
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()









    






                                  





