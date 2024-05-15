# Game "Don't Annoy The Dancer"

This is my first game using PyGame and Pygbag. 
The main sense of the game is turning on and off music and changing songs, 
while the dancer on the screen reacts on your moves. Enjoy!

### Game's Appearance
![image](https://github.com/slothGeorge/Game-Dont-Annoy-The-Dancer/assets/109460766/f25bdf77-1f58-4a39-a35b-dfd6375b7699)

### Instruction
**Active keys**:
* _The "A" key_: turns on previous song from the list of songs
* _The "D" key_: turns on next song from the list of songs
* _The space bar_: turns the music on and off and at the same time stops and forces the dancer to continue walking.
* _The "ESC" key_: exits the game

### deploy virtual environment

```bash
python -m venv venv
```

Activation for **windows**:

```bash
venv/scripts/activate
```

### install libraries

```bash
pip install -r requirements.txt
```

### run pygame

```bash
python game/main.py
```

### build html

```bash
pygbag --build game
```
