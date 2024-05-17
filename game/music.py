import pygame

from constants import music_constants, common_constants


class MusicPlayer:
    """
   Class MusicPlayer is required for interaction with songs:
    loading, changing, stopping and playing
    """
    def __init__(self, song_list):
        pygame.mixer.init()
        self.song_list = song_list
        self.song_index = 0
        self.pos = 0

    def load_music(self):
        """
        The function that loads songs from particular folder
        """
        pygame.mixer.music.load(
            common_constants['CURRENT_FOLDER'] /
            self.song_list[self.song_index])

    def play_music(self):
        """
        The function that plays current song
        """
        self.load_music()
        if self.pos != 0:
            self.play_from_position()
        else:
            pygame.mixer.music.play()

    def stop_music(self):
        """
        The function that stops current song
        """
        self.remember_position()
        pygame.mixer.music.stop()

    def remember_position(self):
        """
        The function remembers where the song stopped
        """
        if pygame.mixer.music.get_busy():
            self.pos = pygame.mixer.music.get_pos()

    def play_from_position(self):
        """
        The function that plays the song
        from the remembered position
        """
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(
                start=self.pos / music_constants['MILLISECONDS_CONVERTER']
            )

    def next_song(self):
        """
        The function that plays the next song from the list of songs
        """
        self.song_index = (self.song_index + 1) % len(self.song_list)
        self.pos = 0
        self.load_music()
        self.play_music()

    def previous_song(self):
        """
        The function that plays the previous song from the list of songs
        """
        self.song_index = (self.song_index - 1) % len(self.song_list)
        self.pos = 0
        self.load_music()
        self.play_music()
