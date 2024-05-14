from pathlib import Path

import pygame

CURRENT_FOLDER = Path(__file__).parent
X_SPEED = 7
X_NO_SPEED = 0
X_DANCER_POS = 160
Y_DANCER_POS = 160


class Dancer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(CURRENT_FOLDER / 'pictures' / 'happy_dancer.png')
        self.original = self.image
        self.stop_image = pygame.image.load(CURRENT_FOLDER / 'pictures' / 'angry_dancer.png')
        self.mirrored_image_right = pygame.transform.flip(self.image, True, False)
        self.mirrored_image_left = self.image
        self.previous_direction = 1
        self.image_gen = self.image_generator()

        self.rect = self.image.get_rect()
        self.x_speed = X_SPEED

        self.scene = pygame.display.get_surface().get_rect()
        self.rect.centerx = self.scene.centerx
        self.rect.y = Y_DANCER_POS

        self.scene = pygame.display.get_surface().get_rect()
        self.rect.x = X_DANCER_POS

    def image_generator(self):
        """
        The function changes the direction of image and yields the right image(mirrored or not)
        """
        if self.x_speed == 0:
            self.x_speed = X_SPEED * self.previous_direction
        while True:
            if self.previous_direction == 1:
                yield self.mirrored_image_left
            else:
                yield self.mirrored_image_right

    def mirror_image(self):
        """
        The function mirrors the image when it collides with the edges of the screen
        """
        if (self.rect.left <= self.scene.left) and (self.x_speed < 0):
            self.previous_direction = 1
            self.x_speed *= -1
            self.image = self.mirrored_image_left
        elif (self.rect.right >= self.scene.right) and (self.x_speed > 0):
            self.previous_direction = -1
            self.x_speed *= -1
            self.image = self.mirrored_image_right

    def update(self):
        """
        The function updates the image
        and depending on the state of music the dancer has speed(music plays) or not(no music)
        """
        if pygame.mixer.music.get_busy():
            self.image_gen = self.image_generator()
            self.image = next(self.image_gen)
            self.mirror_image()
            self.rect.x += self.x_speed
        else:
            self.image = self.stop_image
            self.x_speed = X_NO_SPEED
