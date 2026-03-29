# Lone Wolf Gamebook Assistant

A Flask-based web app that helps you run a Lone Wolf game session by tracking character state, inventory, combat, notes, and saves.

## AI Disclosure

This app was created with AI assistance.

The initial logic and rules source used to build the app is documented in [Instructions.md](Instructions.md).

## How The App Works

The project is split into a small Python backend and a single-page frontend:

- Backend: [app.py](app.py)
  - Serves the main page at `/`
  - Exposes API endpoints for game data and game mechanics
  - Resolves combat rounds using the Lone Wolf combat results table
  - Computes Magnakai Lore Circle bonuses based on selected skills
- Frontend: [templates/index.html](templates/index.html)
  - Renders the full game UI (character sheet, combat panel, inventory, notes, save/load dialogs)
  - Loads game metadata and discipline lists from `/api/game_data`
  - Calls `/api/combat_round` to execute each combat turn
  - Calls `/api/lore_circles` to evaluate Lore Circle bonuses
  - Persists your active state in browser local storage
- Data: [data/kai_ranks.json](data/kai_ranks.json)
  - Provides Kai rank progression data used by the UI and character logic

## Main Features

- Book and subseries support across Kai, Magnakai, Grand Master, and New Order
- Discipline selection with combat-related modifiers
- Random roll utilities for stats/equipment and combat rounds
- Combat resolution with optional modifiers (Psi-surge, Kai-surge, Mindblast, Sommerswerd vs undead)
- Notes tracking for book/page context
- Save and load support in the browser

## API Summary

Defined in [app.py](app.py):

- `GET /api/game_data`: Returns books, disciplines, equipment options, lore circles, and ranks
- `GET /api/roll_random`: Returns a random value (0-9)
- `GET /api/roll_equipment`: Returns two random starting items from the Kai equipment table
- `POST /api/combat_round`: Resolves one combat round and returns updated EP values and outcomes
- `POST /api/lore_circles`: Returns total CS/EP bonuses and completed circle names

## Setup

Install dependencies and create a virtual environment:

### Windows (PowerShell)

```powershell
./setup.ps1
```

### macOS/Linux (bash)

```bash
./setup.sh
```

## Run

### Windows (PowerShell)

```powershell
./run.ps1
```

### macOS/Linux (bash)

```bash
./run.sh
```

Then open http://localhost:5000 in your browser.
