from pathlib import Path

common_constants = {'CURRENT_FOLDER': Path(__file__).parent,
                    }

main_constants = {
    'FPS': 45,
    'SCREEN_SIZE': (1280, 720),
    'ANGRY_DANCER_SOUND': 'angry_dancer_sound.mp3',
    'SONGS': ['1st_song.mp3', '2nd_song.mp3', '3rd_song.mp3'],
    'BACKGROUND_COORDINATES': (0, 0),
    'COLOR_UPPER_TEXT': (252, 3, 3),
    'COLOR_LOWER_TEXT': (237, 79, 12),
    'SIZE_UPPER_TEXT': 50,
    'SIZE_LOWER_TEXT': 38,
    'FILE_PATH_FOR_TEXT': None,
    'ANTIALIAS_FOR_TEXT': True,
    'UPPER_TEXT': "Attention! This guy loves dancing, "
                  "don't you dare turn off the music!",
    'LOWER_TEXT': "To change the music, use the A(<) and D(>) keys, "
                  "and a little advice: DON'T TOUCH THE SPACEBAR!",
    'Y_UPPER_TEXT_POS': 10,
    'Y_LOWER_TEXT_POS': 670,
    'ASYNCIO.SLEEP_DELAY': 0,
}

dancer_constants = {
    'X_SPEED': 7,
    'X_NO_SPEED': 0,
    'X_DANCER_POS': 0,
    'Y_DANCER_POS': 160,
}

music_constants = {
    'MILLISECONDS_CONVERTER': 1000,
}
