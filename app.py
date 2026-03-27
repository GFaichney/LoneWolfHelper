from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
SAVES_DIR = BASE_DIR / "saves"
SAVES_DIR.mkdir(exist_ok=True)
RANKS_FILE = BASE_DIR / "data" / "kai_ranks.json"


def load_kai_ranks() -> dict[str, Any]:
    default = {
        "kai_disciplines": [],
        "magnakai_disciplines": [],
        "grand_master_disciplines": [],
    }
    try:
        payload = json.loads(RANKS_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return default

    ranks = payload.get("lone_wolf_ranks", {})
    if not isinstance(ranks, dict):
        return default

    return {
        "kai_disciplines": ranks.get("kai_disciplines", []),
        "magnakai_disciplines": ranks.get("magnakai_disciplines", []),
        "grand_master_disciplines": ranks.get("grand_master_disciplines", []),
    }


KAI_RANKS = load_kai_ranks()


COMBAT_RATIO_COLUMNS = [
    "<= -11",
    "-10 to -9",
    "-8 to -7",
    "-6 to -5",
    "-4 to -3",
    "-2 to -1",
    "0",
    "+1 to +2",
    "+3 to +4",
    "+5 to +6",
    "+7 to +8",
    "+9 to +10",
    ">= +11",
]

COMBAT_RESULTS_TABLE = {
    "1": [
        {"E": "0", "LW": "K"}, {"E": "0", "LW": "K"}, {"E": "0", "LW": "8"}, {"E": "0", "LW": "6"},
        {"E": "1", "LW": "6"}, {"E": "2", "LW": "5"}, {"E": "3", "LW": "5"}, {"E": "4", "LW": "5"},
        {"E": "5", "LW": "4"}, {"E": "6", "LW": "4"}, {"E": "7", "LW": "4"}, {"E": "8", "LW": "3"},
        {"E": "9", "LW": "3"},
    ],
    "2": [
        {"E": "0", "LW": "K"}, {"E": "0", "LW": "8"}, {"E": "0", "LW": "7"}, {"E": "1", "LW": "6"},
        {"E": "2", "LW": "5"}, {"E": "3", "LW": "5"}, {"E": "4", "LW": "4"}, {"E": "5", "LW": "4"},
        {"E": "6", "LW": "3"}, {"E": "7", "LW": "3"}, {"E": "8", "LW": "3"}, {"E": "9", "LW": "3"},
        {"E": "10", "LW": "2"},
    ],
    "3": [
        {"E": "0", "LW": "8"}, {"E": "0", "LW": "7"}, {"E": "1", "LW": "6"}, {"E": "2", "LW": "5"},
        {"E": "3", "LW": "5"}, {"E": "4", "LW": "4"}, {"E": "5", "LW": "4"}, {"E": "6", "LW": "3"},
        {"E": "7", "LW": "3"}, {"E": "8", "LW": "3"}, {"E": "9", "LW": "2"}, {"E": "10", "LW": "2"},
        {"E": "11", "LW": "2"},
    ],
    "4": [
        {"E": "0", "LW": "8"}, {"E": "1", "LW": "7"}, {"E": "2", "LW": "6"}, {"E": "3", "LW": "5"},
        {"E": "4", "LW": "4"}, {"E": "5", "LW": "4"}, {"E": "6", "LW": "3"}, {"E": "7", "LW": "3"},
        {"E": "8", "LW": "2"}, {"E": "9", "LW": "2"}, {"E": "10", "LW": "2"}, {"E": "11", "LW": "2"},
        {"E": "12", "LW": "2"},
    ],
    "5": [
        {"E": "1", "LW": "7"}, {"E": "2", "LW": "6"}, {"E": "3", "LW": "5"}, {"E": "4", "LW": "4"},
        {"E": "5", "LW": "4"}, {"E": "6", "LW": "3"}, {"E": "7", "LW": "2"}, {"E": "8", "LW": "2"},
        {"E": "9", "LW": "2"}, {"E": "10", "LW": "2"}, {"E": "11", "LW": "2"}, {"E": "12", "LW": "2"},
        {"E": "14", "LW": "1"},
    ],
    "6": [
        {"E": "2", "LW": "6"}, {"E": "3", "LW": "6"}, {"E": "4", "LW": "5"}, {"E": "5", "LW": "4"},
        {"E": "6", "LW": "3"}, {"E": "7", "LW": "2"}, {"E": "8", "LW": "2"}, {"E": "9", "LW": "2"},
        {"E": "10", "LW": "2"}, {"E": "11", "LW": "1"}, {"E": "12", "LW": "1"}, {"E": "14", "LW": "1"},
        {"E": "16", "LW": "1"},
    ],
    "7": [
        {"E": "3", "LW": "5"}, {"E": "4", "LW": "5"}, {"E": "5", "LW": "4"}, {"E": "6", "LW": "3"},
        {"E": "7", "LW": "2"}, {"E": "8", "LW": "2"}, {"E": "9", "LW": "1"}, {"E": "10", "LW": "1"},
        {"E": "11", "LW": "1"}, {"E": "12", "LW": "0"}, {"E": "14", "LW": "0"}, {"E": "16", "LW": "0"},
        {"E": "18", "LW": "0"},
    ],
    "8": [
        {"E": "4", "LW": "4"}, {"E": "5", "LW": "4"}, {"E": "6", "LW": "3"}, {"E": "7", "LW": "2"},
        {"E": "8", "LW": "1"}, {"E": "9", "LW": "1"}, {"E": "10", "LW": "0"}, {"E": "11", "LW": "0"},
        {"E": "12", "LW": "0"}, {"E": "14", "LW": "0"}, {"E": "16", "LW": "0"}, {"E": "18", "LW": "0"},
        {"E": "K", "LW": "0"},
    ],
    "9": [
        {"E": "5", "LW": "3"}, {"E": "6", "LW": "3"}, {"E": "7", "LW": "2"}, {"E": "8", "LW": "0"},
        {"E": "9", "LW": "0"}, {"E": "10", "LW": "0"}, {"E": "11", "LW": "0"}, {"E": "12", "LW": "0"},
        {"E": "14", "LW": "0"}, {"E": "16", "LW": "0"}, {"E": "18", "LW": "0"}, {"E": "K", "LW": "0"},
        {"E": "K", "LW": "0"},
    ],
    "10": [
        {"E": "6", "LW": "0"}, {"E": "7", "LW": "0"}, {"E": "8", "LW": "0"}, {"E": "9", "LW": "0"},
        {"E": "10", "LW": "0"}, {"E": "11", "LW": "0"}, {"E": "12", "LW": "0"}, {"E": "14", "LW": "0"},
        {"E": "16", "LW": "0"}, {"E": "18", "LW": "0"}, {"E": "K", "LW": "0"}, {"E": "K", "LW": "0"},
        {"E": "K", "LW": "0"},
    ],
}

GAMEBOOK_METADATA = [
    {"book_number": 1, "book_name": "Flight from the Dark", "subseries": "Kai"},
    {"book_number": 2, "book_name": "Fire on the Water", "subseries": "Kai"},
    {"book_number": 3, "book_name": "The Caverns of Kalte", "subseries": "Kai"},
    {"book_number": 4, "book_name": "The Chasm of Doom", "subseries": "Kai"},
    {"book_number": 5, "book_name": "Shadow on the Sand", "subseries": "Kai"},
    {"book_number": 6, "book_name": "The Kingdoms of Terror", "subseries": "Magnakai"},
    {"book_number": 7, "book_name": "Castle Death", "subseries": "Magnakai"},
    {"book_number": 8, "book_name": "The Jungle of Horrors", "subseries": "Magnakai"},
    {"book_number": 9, "book_name": "The Cauldron of Fear", "subseries": "Magnakai"},
    {"book_number": 10, "book_name": "The Dungeons of Torgar", "subseries": "Magnakai"},
    {"book_number": 11, "book_name": "The Prisoners of Time", "subseries": "Magnakai"},
    {"book_number": 12, "book_name": "The Masters of Darkness", "subseries": "Magnakai"},
    {"book_number": 13, "book_name": "The Plague Lords of Ruel", "subseries": "Grand Master"},
    {"book_number": 14, "book_name": "The Captives of Kaag", "subseries": "Grand Master"},
    {"book_number": 15, "book_name": "The Darke Crusade", "subseries": "Grand Master"},
    {"book_number": 16, "book_name": "The Legacy of Vashna", "subseries": "Grand Master"},
    {"book_number": 17, "book_name": "The Deathlord of Ixia", "subseries": "Grand Master"},
    {"book_number": 18, "book_name": "Dawn of the Dragons", "subseries": "Grand Master"},
    {"book_number": 19, "book_name": "Wolf's Bane", "subseries": "Grand Master"},
    {"book_number": 20, "book_name": "The Curse of Naar", "subseries": "Grand Master"},
    {"book_number": 21, "book_name": "Voyage of the Moonstone", "subseries": "New Order"},
    {"book_number": 22, "book_name": "The Buccaneers of Shadaki", "subseries": "New Order"},
    {"book_number": 23, "book_name": "Mydnight's Hero", "subseries": "New Order"},
    {"book_number": 24, "book_name": "Rune War", "subseries": "New Order"},
    {"book_number": 25, "book_name": "Trail of the Wolf", "subseries": "New Order"},
    {"book_number": 26, "book_name": "The Fall of Blood Mountain", "subseries": "New Order"},
    {"book_number": 27, "book_name": "Vampirium", "subseries": "New Order"},
    {"book_number": 28, "book_name": "The Hunger of Sejanoz", "subseries": "New Order"},
    {"book_number": 29, "book_name": "The Storms of Chai", "subseries": "New Order"},
    {"book_number": 30, "book_name": "Dead in the Deep", "subseries": "New Order"},
    {"book_number": 31, "book_name": "The Dusk of Eternal Night", "subseries": "New Order"},
    {"book_number": 32, "book_name": "Light of the Kai", "subseries": "New Order"},
]

KAI_SKILLS = {
    "kai_disciplines": [
        "Camouflage", "Hunting", "Sixth Sense", "Tracking", "Healing", "Weaponskill",
        "Mindblast", "Animal Kinship", "Mind Over Matter", "Mindshield",
    ],
    "magnakai_disciplines": [
        "Weaponmastery", "Animal Control", "Curing", "Invisibility", "Huntmastery",
        "Pathsmanship", "Psi-surge", "Psi-screen", "Nexus", "Divination",
    ],
    "grand_master_disciplines": [
        "Grand Weaponmastery", "Animal Mastery", "Deliverance", "Assimilance", "Grand Huntmastery",
        "Grand Pathsmanship", "Kai-surge", "Kai-screen", "Grand Nexus", "Telegnosis",
    ],
    "new_order_grand_master_disciplines": [
        "Magi-magic", "Kai-alchemy", "Astrology", "Herbmastery", "Elementalism", "Bardsmanship",
    ],
    "magnakai_lore_circles": [
        {
            "name": "Circle of Fire",
            "required_disciplines": ["Weaponmastery", "Huntmastery"],
            "bonus_cs": 1,
            "bonus_ep": 2,
        },
        {
            "name": "Circle of Light",
            "required_disciplines": ["Animal Control", "Curing"],
            "bonus_cs": 0,
            "bonus_ep": 3,
        },
        {
            "name": "Circle of Solaris",
            "required_disciplines": ["Invisibility", "Huntmastery", "Pathsmanship"],
            "bonus_cs": 1,
            "bonus_ep": 3,
        },
        {
            "name": "Circle of Spirit",
            "required_disciplines": ["Psi-surge", "Psi-screen", "Nexus", "Divination"],
            "bonus_cs": 3,
            "bonus_ep": 3,
        },
    ],
}


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/api/bootstrap", methods=["GET"])
def bootstrap() -> Any:
    payload = {
        "gamebook_metadata": GAMEBOOK_METADATA,
        "kai_skills": KAI_SKILLS,
        "kai_ranks": KAI_RANKS,
        "combat": {
            "columns_combat_ratio": COMBAT_RATIO_COLUMNS,
            "results_by_roll": COMBAT_RESULTS_TABLE,
        },
        "inventory_rules": {
            "max_backpack_items": 8,
            "max_weapons": 2,
            "max_gold": 50,
            "max_special_items": 12,
            "max_arrows_per_quiver": 6,
        },
    }
    return jsonify(payload)


def safe_slug(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9 _-]", "", text).strip()
    return re.sub(r"\s+", "_", cleaned)[:60] or "session"


def get_book_name(book_number: int) -> str:
    for book in GAMEBOOK_METADATA:
        if book["book_number"] == book_number:
            return book["book_name"]
    return f"Book_{book_number}"


@app.route("/api/saves", methods=["GET"])
def list_saves() -> Any:
    files = sorted(SAVES_DIR.glob("*.json"), key=lambda f: f.stat().st_mtime, reverse=True)
    save_entries: list[dict[str, Any]] = []
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            save_entries.append(
                {
                    "filename": path.name,
                    "save_name": data.get("save_name", path.stem),
                    "book_number": data.get("book_number"),
                    "book_name": data.get("book_name"),
                    "page_number": data.get("page_number"),
                    "created_at": data.get("created_at"),
                }
            )
        except (json.JSONDecodeError, OSError):
            continue
    return jsonify({"saves": save_entries})


@app.route("/api/save", methods=["POST"])
def save_game() -> Any:
    body = request.get_json(silent=True) or {}
    state = body.get("state")
    if not isinstance(state, dict):
        return jsonify({"error": "State payload is required."}), 400

    session_name = str(body.get("session_name", "session")).strip()
    book_number = int(body.get("book_number", 1))
    page_number = int(body.get("page_number", 1))

    book_name = get_book_name(book_number)
    file_name = f"{safe_slug(book_name)}-p{page_number}-{safe_slug(session_name)}.json"
    save_path = SAVES_DIR / file_name

    save_payload = {
        "save_name": f"{book_name} p.{page_number} {session_name}",
        "book_number": book_number,
        "book_name": book_name,
        "page_number": page_number,
        "session_name": session_name,
        "created_at": body.get("created_at"),
        "state": state,
    }

    save_path.write_text(json.dumps(save_payload, indent=2), encoding="utf-8")
    return jsonify({"ok": True, "filename": file_name, "save_name": save_payload["save_name"]})


@app.route("/api/load", methods=["POST"])
def load_game() -> Any:
    body = request.get_json(silent=True) or {}
    filename = str(body.get("filename", "")).strip()
    if not filename:
        return jsonify({"error": "A save filename is required."}), 400

    save_path = (SAVES_DIR / filename).resolve()
    if save_path.parent != SAVES_DIR.resolve() or not save_path.exists():
        return jsonify({"error": "Save file not found."}), 404

    data = json.loads(save_path.read_text(encoding="utf-8"))
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
