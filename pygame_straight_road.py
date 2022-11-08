import math

import pygame
import sys
import time

from main import *

POSITION = 10
POS_Y = 250
CLOCK = 0.2


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos * POSITION, POS_Y)


class SimulationGame:

    def __init__(self):
        self.lane = create_lane()
        self.car_list = []
        self.moving_sprites = None
        self.screen = None

    def insert_cars(self, car_list):
        insert_car(self.lane, car_list)

    def pygame_setup(self):
        # General Setup
        pygame.init()

        # Game Screen
        screen_width = 1000
        screen_height = 500
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Sprite Animation")

        # Creating the sprites and groups
        self.moving_sprites = pygame.sprite.Group()

    def mainloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # background
            self.screen.fill((0, 255, 255))
            self.moving_sprites.draw(self.screen)

            pygame.display.flip()
            # pygame.display.update()

            # step
            self.pygame_step()

            time.sleep(CLOCK)


    def pygame_step(self):
        self.moving_sprites.empty()
        updated_lane = step(self.lane)
        for i in range(LANE_SIZE):
            if updated_lane[i] == OCCUPIED:
                new_rectangle = Rectangle(int(i))
                self.moving_sprites.add(new_rectangle)
                # print(new_rectangle, " ", new_rectangle.rect)
        self.lane = updated_lane


if __name__ == '__main__':
    car1 = Car(0, 3)
    car2 = Car(6, 3)
    car3 = Car(44, 2)
    car4 = Car(55, 3)
    car5 = Car(77, 4)
    index_list = [car1, car2, car3, car4, car5]
    car_l = [car1]

    sim = SimulationGame()
    sim.pygame_setup()
    sim.insert_cars(index_list)
    sim.mainloop()