from pathlib import Path

import pygame

CURRENT_FOLDER = Path(__file__).parent


class MusicPlayer:
    def __init__(self, song_list):
        pygame.mixer.init()
        self.song_list = song_list
        self.song_index = 0
        self.pos = 0

    def load_music(self):
        pygame.mixer.music.load(CURRENT_FOLDER / 'Songs' / self.song_list[self.song_index])

    def play_music(self):
        self.load_music()
        if self.pos != 0:
            self.play_from_position()
        else:
            pygame.mixer.music.play()

    def stop_music(self):
        self.remember_position()
        pygame.mixer.music.stop()

    def remember_position(self):
        if pygame.mixer.music.get_busy():
            self.pos = pygame.mixer.music.get_pos()

    def play_from_position(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(start=self.pos / 1000.0)

    def next_song(self):
        self.song_index = (self.song_index + 1) % len(self.song_list)
        self.pos = 0
        self.load_music()
        self.play_music()

    def previous_song(self):
        self.song_index = (self.song_index - 1) % len(self.song_list)
        self.pos = 0
        self.load_music()
        self.play_music()
