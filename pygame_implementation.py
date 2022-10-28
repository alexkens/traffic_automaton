import pygame
import sys
import time

from main import *



class Rectangle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([100, 100])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]


# Grid Setup
lane = create_lane()

car1 = Car(4, 1)
car2 = Car(6, 2)
car3 = Car(44, 5)
car4 = Car(55, 3)
car5 = Car(77, 4)

index_list = [car1, car2, car3, car4, car5]

insert_car(lane, index_list)

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()


"""def pygame_step(grid, moving_sprites):
    moving_sprites.empty()
    for i in range(100):
        if grid[i] == ALIVE:
            j = i % BASE
            rectangle_tmp = Rectangle(j * BASE * BASE, (i-j) * BASE)
            moving_sprites.add(rectangle_tmp)
            print(i)
            print(j, " ", i-j)
            print()
"""

# mainloop
"""i = 0
j = 0"""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    """rectangle1.rect.topleft = [i, j*10]
    i += 1
    if i % 1000 == 0:
        i = 0
        j += 1
    print(i)"""

    """pygame_step(grid, moving_sprites)
    grid = step(grid)

    screen.fill((0, 255, 255))
    moving_sprites.draw(screen)
    pygame.display.flip()"""

    # clock.tick(1000000)
    time.sleep(0.5)