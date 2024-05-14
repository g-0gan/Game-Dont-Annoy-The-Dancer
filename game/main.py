"""
This is my first simple game that based on pygame and pygbag.
There are A and D keys(changing songs) and Spacebar(stop and play music)
When the music doesn't play dancer stops, and you have made him angry!
"""
import asyncio
import sys
from pathlib import Path

import pygame

from constants import main_constants
from dancing_guy import Dancer
from music import MusicPlayer

CURRENT_FOLDER = Path(__file__).parent
MUSIC_PLAYER = MusicPlayer(main_constants['SONGS'])
KEY_ACTIONS = {
    pygame.K_a: MUSIC_PLAYER.previous_song,
    pygame.K_d: MUSIC_PLAYER.next_song,
    pygame.K_SPACE:
        (lambda:
         MUSIC_PLAYER.stop_music() if pygame.mixer.music.get_busy()
         else MUSIC_PLAYER.play_music()),
    pygame.K_ESCAPE: sys.exit
}


def render_text(file_path, size, text, antialias, color, centerx, y):
    font = pygame.font.Font(file_path, size)
    rendered_text = font.render(text, antialias, color)
    textpos = rendered_text.get_rect(centerx=centerx, y=y)
    return rendered_text, textpos


async def main():
    pygame.init()
    screen: pygame.Surface = (pygame.display.set_mode
                              (main_constants['SCREEN_SIZE']))
    clock = pygame.time.Clock()

    pygame.mixer.init()
    MUSIC_PLAYER.play_music()
    dancer = Dancer()
    all_sprites = pygame.sprite.RenderPlain(dancer)

    background = pygame.image.load(
        CURRENT_FOLDER /
        'pictures' /
        'dance_floor.jpg')
    screen.blit(background, main_constants['BACKGROUND_COORDINATES'])
    pygame.display.update()

    if pygame.font:
        text, textpos = render_text(
            main_constants['FILE_PATH_FOR_TEXT'],
            main_constants['SIZE_UPPER_TEXT'],
            main_constants['UPPER_TEXT'],
            main_constants['ANTIALIAS_FOR_TEXT'],
            main_constants['COLOR_UPPER_TEXT'],
            background.get_width() / 2,
            main_constants['Y_UPPER_TEXT_POS']
        )
        background.blit(text, textpos)

        text, textpos = render_text(
            main_constants['FILE_PATH_FOR_TEXT'],
            main_constants['SIZE_LOWER_TEXT'],
            main_constants['LOWER_TEXT'],
            main_constants['ANTIALIAS_FOR_TEXT'],
            main_constants['COLOR_LOWER_TEXT'],
            background.get_width() / 2,
            main_constants['Y_LOWER_TEXT_POS']
        )
        background.blit(text, textpos)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                action = KEY_ACTIONS.get(event.key)
                if action:
                    action()

        all_sprites.update()
        screen.blit(background, main_constants['BACKGROUND_COORDINATES'])
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(main_constants['FPS'])
        await asyncio.sleep(main_constants['ASYNCIO.SLEEP_DELAY'])

if __name__ == '__main__':
    asyncio.run(main())
