# ChoccyMilk's Asteroids

A classic arcade space shooter game built in Python, based on a guided tutorial from boot.dev, but with several added features and improvements.

**(Optional: Consider adding a screenshot or GIF here!)**

## About This Project

This project started as a recreation of the original Asteroids game following a tutorial from boot.dev. I have since expanded upon the base tutorial, adding new features and refining existing ones.

## Features

* **Classic Asteroids Gameplay:** Pilot a ship, destroy asteroids, and avoid collisions.
* **Added Features:**
  * Game Timer
  * Time-based Score Multiplier
  * Persistent High Score Tracking
  * Accurate Triangle Hitbox (Improved from the tutorial's circular hitbox to match the player sprite)
  * Functional HUD Settings Menu
  * Basic Local Multiplayer Mode (Work in Progress)

For planned features, please see the `TODO.md` file (or link it: `[TODO.md](TODO.md)`).

## Prerequisites

* Python 3.x (Specify version if known, e.g., Python 3.8+)
* `pip` or `uv` for installing dependencies

## Installation

1. **Clone the repository:**

    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

2. **Set up a virtual environment (Recommended):**

    ```bash
    # Using Python's built-in venv
    python3 -m venv .venv
    source .venv/bin/activate # On Windows use `.venv\Scripts\activate`

    # Or using uv
    uv venv
    source .venv/bin/activate # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies:** Choose one of the following methods:
    * **Using uv (Recommended if you have it):**

        ```bash
    uv pip install .
        ```

    * **Using pip:**

        ```bash
        pip install .
        ```

## Running the Game

1. Make sure your virtual environment is activated.
2. Run the main menu script:

    ```bash
    python3 menu.py
    ```

    or

    ```
    # uv run menu.py
    ```

3. You should now be in the game menu. Currently, the only complete mode is Single Player Survival. Multiplayer Survival allows local co-op play but the HUD is still under development.

## Controls

### Player 1 / Single Player

* `W` - Move forward
* `A` - Turn left
* `S` - Move backward
* `D` - Turn right
* `Space` - Shoot

### Player 2 (Local Multiplayer)

* `Up Arrow` - Move forward
* `Left Arrow` - Turn left
* `Down Arrow` - Move backward
* `Right Arrow` - Turn right
* `Enter` - Shoot
