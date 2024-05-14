from pathlib import Path

import pygame

CURRENT_FOLDER = Path(__file__).parent


class Dancer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(CURRENT_FOLDER / 'Pictures' / 'happy_dancer.png')
        self.stop_image = pygame.image.load(CURRENT_FOLDER / 'Pictures' / 'angry_dancer.png')
        self.mirrored_image = pygame.transform.flip(self.image, True, False)

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
        image = self.image
        speed = 8
        self.rect.x += self.x_speed
        if pygame.mixer.music.get_busy():
            self.image = image
            self.x_speed = speed
            if self.rect.right > self.scene.right:
                self.rect.right = self.scene.right
                self.x_speed *= -1
                self.image = self.mirrored_image
            if self.rect.left < self.scene.left:
                self.rect.left = self.scene.left
                self.x_speed *= -1
                self.image = self.mirrored_image
        else:
            self.image = self.stop_image
            self.x_speed = 0

