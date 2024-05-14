"""
This is my first simple game that based on pygame.`
"""
import asyncio
import sys
from pathlib import Path

import pygame

from dancing_guy import Dancer
from music import MusicPlayer

FPS = 45
SCREEN_SIZE = (1280, 720)

CURRENT_FOLDER = Path(__file__).parent
SONGS = ['1st_song.mp3', '2nd_song.mp3', '3rd_song.mp3']

music_player = MusicPlayer(SONGS)


async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    background = pygame.image.load(CURRENT_FOLDER / 'Pictures' / 'dance_floor.jpg')
    screen.blit(background, (0, 0))
    pygame.display.update()

    dancer = Dancer()  # Sprite: Surface, Rectangle
    all_sprites = pygame.sprite.RenderPlain(dancer)

    if pygame.font:
        font = pygame.font.Font(None, 50)
        text = font.render("Attention! This guy loves dancing, don't you dare turn off the music!", True, (252, 3, 3))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        background.blit(text, textpos)

        font = pygame.font.Font(None, 38)
        text = font.render(
            "To change the music, use the A(<) and D(>) keys, and a little advice: DON'T TOUCH THE SPACEBAR!",
            True,
            (237, 79, 12))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=670)
        background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    pygame.mixer.init()
    music_player.play_music()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    music_player.previous_song()
                if event.key == pygame.K_d:
                    music_player.next_song()
                if event.key == pygame.K_SPACE:
                    if pygame.mixer.music.get_busy():
                        music_player.stop_music()
                    else:
                        music_player.play_music()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        all_sprites.update()

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
