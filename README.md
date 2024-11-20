# NinjaMultiplayer
A 2D ninja game for two players in local multiplayer.
Built with Python (Pygame Zero).

## Requirements
- Python 3.x
- Pygame Zero

## Compatibility Note
If you're using an OS other than macOS, please modify the `Ninja.py` file as follows:

- **Delete line 1:** `import os`  
- **Delete line 2:** `os.environ["SDL_VIDEO_WINDOW_POS"] = "50, 100"`

This ensures the game works correctly on other platforms.

## How to Run
1. Install *Pygame Zero*: `pip install pgzero`
2. Run the Code: `pgzrun Ninja.py`

Enjoy!
