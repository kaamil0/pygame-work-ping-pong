import pygame 
import random
pygame.init()


# Game Configurations 
WIDTH = 800
HEIGHT = 600
TITLE = "Super Dodge 2"
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# ------------------ COLOURS ------------------
# Background
BG_COLOUR = (15, 15, 25) # Dark Blue/Black

# Player
PLAYER_COLOUR = (255, 0, 100) # Hot Pink

def collision(collision_type):
    global Player_speed_x, Player_speed_y,Player_base_speed

    if collision_type == "wall":
        ball_speed_y *= -1
    if collision_type == "player":
        Player_speed_x = Player_base_speed * random.choice((1, -1))
        Player_speed_y = Player_base_speed * random.choice((1, -1))
        Player_speed_x *= -1


# -------------------- Player -------------------
class Player:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.colour = PLAYER_COLOUR
        self.rect = pygame.Rect(WIDTH // 2 - (self.width // 2), HEIGHT - self.height, self.width, self.height)
        self.speed = 9
        if Player <= 0 or Player >=HEIGHT:
            ("collision")
            

    def create(self):
        pygame.draw.rect(screen, self.colour, self.rect, border_radius=8)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.y -= self.speed




ohn = Player()
        



running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            
            
    keys = pygame.key.get_pressed()

    ohn.move(keys)

    screen.fill(BG_COLOUR) 


    # Draw on the screen
    ohn.create()


    pygame.display.update()

pygame.quit()
