from pathlib import Path

import pygame

CURRENT_FOLDER = Path(__file__).parent


class Dancer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(CURRENT_FOLDER / 'Pictures' / 'happy_dancer.png')
        self.original = self.image
        self.stop_image = pygame.image.load(CURRENT_FOLDER / 'Pictures' / 'angry_dancer.png')
        self.mirrored_image_right = pygame.transform.flip(self.image, True, False)
        self.mirrored_image_left = self.image
        self.previous_direction = 1
        self.image_gen = self.image_generator()

        self.rect = self.image.get_rect()
        self.x_speed = 7

        self.scene = pygame.display.get_surface().get_rect()
        self.rect.centerx = self.scene.centerx
        self.rect.y = 100

        self.scene = pygame.display.get_surface().get_rect()
        self.rect.centerx = self.scene.centerx
        self.rect.x = 100

        self.scene = pygame.display.get_surface().get_rect()
        self.rect.centerx = self.scene.centerx

    def image_generator(self):
        if self.x_speed == 0:
            self.x_speed = 7 * self.previous_direction
        while True:
            if self.previous_direction == 1:
                yield self.mirrored_image_left
            else:
                yield self.mirrored_image_right

    def mirror_image(self):
        if (self.rect.left <= self.scene.left) and (self.x_speed < 0):
            self.previous_direction = 1
            self.x_speed *= -1
            self.image = self.mirrored_image_left
        elif (self.rect.right >= self.scene.right) and (self.x_speed > 0):
            self.previous_direction = -1
            self.x_speed *= -1
            self.image = self.mirrored_image_right

    def update(self):
        if pygame.mixer.music.get_busy():
            self.image_gen = self.image_generator()
            self.image = next(self.image_gen)
            self.mirror_image()
            self.rect.x += self.x_speed
        else:
            self.image = self.stop_image
            self.x_speed = 0

