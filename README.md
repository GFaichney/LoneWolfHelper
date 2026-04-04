# Lone Wolf Gamebook Assistant

A Flask-based web app that helps you run a Lone Wolf game session by tracking character state, inventory, combat, notes, and saves.

## AI Disclosure

This app was created with AI assistance.

The initial logic and rules source used to build the app is documented in [Instructions.md](Instructions.md).

## How The App Works

The project is split into a small Python backend and a single-page frontend:

- Backend: [app.py](app.py)
  - Serves the main page at `/`
  - Exposes API endpoints for game data, combat mechanics, and filesystem save files
  - Resolves combat rounds using the Lone Wolf combat results table
  - Computes Magnakai Lore Circle bonuses based on selected skills
- Frontend: [templates/index.html](templates/index.html)
  - Renders the full game UI (character sheet, combat panel, inventory, notes, save/load dialogs)
  - Loads game metadata and discipline lists from `/api/game_data`
  - Calls `/api/combat_round` to execute each combat turn
  - Calls `/api/lore_circles` to evaluate Lore Circle bonuses
  - Persists active in-progress state in browser local storage (`lw_state`)
  - Uses backend save APIs for named save files on disk
- Data: [data/kai_ranks.json](data/kai_ranks.json)
  - Provides Kai rank progression data used by the UI and character logic

## Save Storage Model

There are two kinds of persistence:

- **Autosave/working state (browser):** stored in `localStorage` under key `lw_state`
- **Named save slots (filesystem):** stored as JSON files in `saves/` in the project root

When you load a save from disk and then click **Save** again:
- the **Session Name** is pre-populated from the loaded save
- the same save file is overwritten (instead of creating a new slot)

## Main Features

- Book and subseries support across Kai, Magnakai, Grand Master, and New Order
- Character creation and progression by subseries discipline rules
- Book switching flow with:
  - completed books tracking
  - gold transition rolls
  - special-item carry-over filtering by subseries rules
  - discipline gains on progression
  - Grand Master backpack capacity increase (to 10)
- Kai Monastery support:
  - transfer to/from monastery during book switching
  - read-only monastery view in Inventory tab outside switching
- Random roll utilities:
  - global quick roll button (0–9) at the top
  - stat/equipment and combat-related random endpoints
- Combat resolution with optional modifiers (Psi-surge, Kai-surge, Mindblast, Sommerswerd vs undead)
  - player Mindblast checkbox shown only when learned
  - Mindblast gives +2 CS and costs 2 EP per round
  - round roll is blocked if Mindblast is checked and EP < 2
- Notes tracking for book/page context
- Save/load from JSON files on disk

## API Summary

Defined in [app.py](app.py):

- `GET /api/game_data`: Returns books, disciplines, equipment options, lore circles, and ranks
- `GET /api/roll_random`: Returns a random value (0-9)
- `GET /api/roll_equipment`: Returns two random starting items from the Kai equipment table
- `POST /api/combat_round`: Resolves one combat round and returns updated EP values and outcomes
- `POST /api/lore_circles`: Returns total CS/EP bonuses and completed circle names
- `GET /api/saves`: Returns metadata for all save files in `saves/`
- `POST /api/saves`: Creates a new save file
- `GET /api/saves/<save_id>`: Returns a full save (including `state`)
- `PUT /api/saves/<save_id>`: Overwrites an existing save file
- `DELETE /api/saves/<save_id>`: Deletes an existing save file

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

## Notes

- Ensure you run setup before run so Flask and dependencies are installed.
- The `saves/` folder is created automatically when needed.
