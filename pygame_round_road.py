import math

import pygame
import sys
import time

from main import *

POSITION = 10
POS_Y = 250
CLOCK = 0.09
PNG_PATH = 'limousine.png'


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos, POS_Y)


class RectangleImage(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        car_img = pygame.image.load(PNG_PATH)
        DEFAULT_IMAGE_SIZE = (40, 40)
        car_img = pygame.transform.scale(car_img, DEFAULT_IMAGE_SIZE)
        self.image = car_img
        self.rect = self.image.get_rect()
        # self.rect.center = (pos, POS_Y)

        self.rect.center = int_to_degree_to_coord(pos)

        #print("pos: ", pos," center: ", self.rect.center)


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
        screen_width = 500
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
            self.screen.fill("green")
            # self.moving_sprites.draw(self.screen)



            # Set the circle road
            circle = pygame.draw.circle(self.screen, "grey", (250., 250.), 225., 50)
            self.moving_sprites.draw(self.screen)
            pygame.display.flip()
            # pygame.display.update()
            blits_list = []
            #for img in self.moving_sprites:
                #img = RectangleImage(img)
                # blits_list.append((img, img.rect.center))
            #self.screen.blits(blits_list)

            #
            # step
            self.pygame_step(circle)

            time.sleep(CLOCK)

            """screen.fill(GRAY)
            screen.blit(img, rect)
            pygame.draw.rect(screen, RED, rect, 1)
            pygame.display.update()"""

    def pygame_step(self, circle):
        self.moving_sprites.empty()
        updated_lane = step(self.lane)
        for i in range(LANE_SIZE):
            if updated_lane[i] == OCCUPIED:
                new_rectangle = RectangleImage(int(i)) # * POSITION
                self.moving_sprites.add(new_rectangle)
                # print(new_rectangle, " ", new_rectangle.rect)
        self.lane = updated_lane


def int_to_degree_to_coord(pos):
    degree = pos * 3.6
    h = 400/2
    x = math.cos(math.radians(degree)) * h
    y_temp = h*h - x*x
    y = math.sqrt(y_temp)

    if pos > 50:
        y = y * -1

    print("pos: ", pos, ", x: ", x, ", y: ", y)
    return tuple((x + 250, y + 250))


if __name__ == '__main__':
    car1 = Car(0, 3)
    car2 = Car(26, 3)
    car3 = Car(44, 3)
    car4 = Car(55, 3)
    car5 = Car(99, 3)
    index_list = [car1, car2, car3, car4, car5]
    car_l = [car1]

    sim = SimulationGame()
    sim.pygame_setup()
    sim.insert_cars(index_list)
    sim.mainloop()