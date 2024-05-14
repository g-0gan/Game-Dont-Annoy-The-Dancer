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
        self.mirrored_image_left = pygame.transform.flip(self.image, True, False)
        self.previous_direction = 1

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

    def update(self):
        image = pygame.image.load(CURRENT_FOLDER / 'Pictures' / 'happy_dancer.png')
        if pygame.mixer.music.get_busy():
            if self.image == self.stop_image:
                self.image = image
            if self.x_speed == 0:
                self.x_speed = 7 * self.previous_direction
            if (self.rect.left <= self.scene.left) and (self.x_speed < 0):
                self.previous_direction = 1
                self.x_speed *= -1
                self.image = self.image = self.mirrored_image_left
            elif (self.rect.right >= self.scene.right) and (self.x_speed > 0):
                self.previous_direction = -1
                self.x_speed *= -1
                self.image = self.mirrored_image_left
            self.rect.x += self.x_speed
        else:
            self.image = self.stop_image
            self.x_speed = 0

