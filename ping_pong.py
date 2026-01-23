import pygame 
import random

pygame.init()

# Game variables
WIDTH = 900
HEIGHT = 600
FPS = 60


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong of the Tairus")
clock = pygame.time.Clock()


# Ball Properties 
ball_colour = "green"
ball_speed_x = 4 * random.choice((1, -1))
ball_speed_y = 4 * random.choice((1, -1))
ball_radius = 18

ball = pygame.Rect(WIDTH//2, HEIGHT//2, ball_radius, ball_radius)


def centre_ball():
    global ball, ball_speed_x, ball_speed_y
    ball.center= (WIDTH//2, HEIGHT//2)

    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

def animate_ball(): 
    global ball
    ball.x += ball_speed_x 
    ball.y += ball_speed_y 

def reverse_bounce_ball(collision_type):
    global ball_speed_x, ball_speed_y
    if collision_type == "wall":
        ball_speed_y *= -1
    if collision_type == "player":
        ball_speed_x *= -1


# Universal properites for Players 
player_width = 10
player_height = 120
player_speed = 6



# Kaamil's Properties
kaamil_colour = "white"

# Khalid's Properitesd 
khalid_colour = "blue"



kaamil = pygame.Rect(10, HEIGHT//2 - player_height //2, player_width, player_height)
khalid = pygame.Rect(WIDTH - player_width - 10, HEIGHT//2 - player_height //2, player_width, player_height)

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        animate_ball()
        
        if ball.x <= 0 or ball.x >= WIDTH:
            centre_ball()
        if ball.y <= 0 or ball.y >= HEIGHT:
            reverse_bounce_ball("wall")

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and khalid.top > 0:
            khalid.y -= player_speed

        if keys[pygame.K_DOWN] and khalid.bottom < HEIGHT:
            khalid.y += player_speed

        if keys[pygame.K_w] and kaamil.top > 0:
            kaamil.y -= player_speed

        if keys[pygame.K_s] and kaamil.bottom < HEIGHT:
            kaamil.y += player_speed

        if ball.colliderect(kaamil) or ball.colliderect(khalid):
            reverse_bounce_ball("player")

        screen.fill("black")


        # Draw visuals
        
        pygame.draw.line(screen, "gray", (WIDTH//2 , 0), (WIDTH //2, HEIGHT), 2 )

        pygame.draw.rect(screen, kaamil_colour, kaamil)
        pygame.draw.rect(screen, khalid_colour, khalid)
        pygame.draw.ellipse(screen, ball_colour, ball)
        pygame.display.flip()

        clock.tick(70)



            
    

if __name__ == "__main__":
    main()
