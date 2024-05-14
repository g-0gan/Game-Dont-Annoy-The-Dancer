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
key_actions = {
    pygame.K_a: MUSIC_PLAYER.previous_song,
    pygame.K_d: MUSIC_PLAYER.next_song,
    pygame.K_ESCAPE: sys.exit
}


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
        font = pygame.font.Font(main_constants['FILE_PATH_FOR_TEXT'],
                                main_constants['SIZE_UPPER_TEXT'])
        text = font.render(main_constants['UPPER_TEXT'],
                           main_constants['ANTIALIAS_FOR_TEXT'],
                           main_constants['COLOR_UPPER_TEXT'])
        textpos = text.get_rect(centerx=background.get_width() / 2,
                                y=main_constants['Y_UPPER_TEXT_POS'])
        background.blit(text, textpos)

        font = pygame.font.Font(main_constants['FILE_PATH_FOR_TEXT'],
                                main_constants['SIZE_LOWER_TEXT'])
        text = font.render(
            main_constants['LOWER_TEXT'],
            main_constants['ANTIALIAS_FOR_TEXT'],
            main_constants['COLOR_LOWER_TEXT'])
        textpos = text.get_rect(centerx=background.get_width() / 2,
                                y=main_constants['Y_LOWER_TEXT_POS'])
        background.blit(text, textpos)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                action = key_actions.get(event.key)
                if action:
                    action()
                elif event.key == pygame.K_SPACE:
                    if pygame.mixer.music.get_busy():
                        MUSIC_PLAYER.stop_music()
                    else:
                        MUSIC_PLAYER.play_music()

        all_sprites.update()
        screen.blit(background, main_constants['BACKGROUND_COORDINATES'])
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(main_constants['FPS'])
        await asyncio.sleep(main_constants['ASYNCIO.SLEEP_DELAY'])


if __name__ == '__main__':
    asyncio.run(main())
