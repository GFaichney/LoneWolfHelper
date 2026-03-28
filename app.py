import json
import os
import random
from flask import Flask, jsonify, request, render_template, send_from_directory

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Game Data
# ---------------------------------------------------------------------------

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

KAI_DISCIPLINES = [
    {"name": "Camouflage", "combat_bonus": None},
    {"name": "Hunting", "combat_bonus": None},
    {"name": "Sixth Sense", "combat_bonus": None},
    {"name": "Tracking", "combat_bonus": None},
    {"name": "Healing", "combat_bonus": None},
    {"name": "Weaponskill", "combat_bonus": "+2 CS with mastered weapon"},
    {"name": "Mindblast", "combat_bonus": "+2 CS (vs non-immune)"},
    {"name": "Animal Kinship", "combat_bonus": None},
    {"name": "Mind Over Matter", "combat_bonus": None},
    {"name": "Mindshield", "combat_bonus": "Prevents psychic EP loss"},
]

MAGNAKAI_DISCIPLINES = [
    {"name": "Weaponmastery", "combat_bonus": "+3 CS with mastered weapons"},
    {"name": "Animal Control", "combat_bonus": None},
    {"name": "Curing", "combat_bonus": "Restores 1 EP per section without combat"},
    {"name": "Invisibility", "combat_bonus": None},
    {"name": "Huntmastery", "combat_bonus": None},
    {"name": "Pathsmanship", "combat_bonus": None},
    {"name": "Psi-surge", "combat_bonus": "+4 CS / costs 2 EP per round"},
    {"name": "Psi-screen", "combat_bonus": "Absorbs psychic damage"},
    {"name": "Nexus", "combat_bonus": None},
    {"name": "Divination", "combat_bonus": None},
]

MAGNAKAI_LORE_CIRCLES = [
    {"name": "Circle of Fire", "required": ["Weaponmastery", "Huntmastery"], "cs_bonus": 1, "ep_bonus": 2},
    {"name": "Circle of Light", "required": ["Animal Control", "Curing"], "cs_bonus": 0, "ep_bonus": 3},
    {"name": "Circle of Solaris", "required": ["Invisibility", "Huntmastery", "Pathsmanship"], "cs_bonus": 1, "ep_bonus": 3},
    {"name": "Circle of Spirit", "required": ["Psi-surge", "Psi-screen", "Nexus", "Divination"], "cs_bonus": 3, "ep_bonus": 3},
]

GRAND_MASTER_DISCIPLINES = [
    {"name": "Grand Weaponmastery", "combat_bonus": "+5 CS with any weapon"},
    {"name": "Animal Mastery", "combat_bonus": None},
    {"name": "Deliverance", "combat_bonus": "Can restore up to 20 EP (once per adventure)"},
    {"name": "Assimilance", "combat_bonus": None},
    {"name": "Grand Huntmastery", "combat_bonus": None},
    {"name": "Grand Pathsmanship", "combat_bonus": None},
    {"name": "Kai-surge", "combat_bonus": "+8 CS / costs 1 EP per round"},
    {"name": "Kai-screen", "combat_bonus": "Negates psychic CS/EP loss"},
    {"name": "Grand Nexus", "combat_bonus": None},
    {"name": "Telegnosis", "combat_bonus": None},
]

NEW_ORDER_DISCIPLINES = [
    {"name": "Magi-magic", "combat_bonus": "Varies by spell"},
    {"name": "Kai-alchemy", "combat_bonus": "Magical attacks"},
    {"name": "Astrology", "combat_bonus": None},
    {"name": "Herbmastery", "combat_bonus": None},
    {"name": "Elementalism", "combat_bonus": "Destroy/manipulate enemy equipment"},
    {"name": "Bardsmanship", "combat_bonus": "Can pacify enemies"},
]

COMBAT_RESULTS_TABLE = {
    "1":  [{"E":"0","LW":"K"},{"E":"0","LW":"K"},{"E":"0","LW":"8"},{"E":"0","LW":"6"},{"E":"1","LW":"6"},{"E":"2","LW":"5"},{"E":"3","LW":"5"},{"E":"4","LW":"5"},{"E":"5","LW":"4"},{"E":"6","LW":"4"},{"E":"7","LW":"4"},{"E":"8","LW":"3"},{"E":"9","LW":"3"}],
    "2":  [{"E":"0","LW":"K"},{"E":"0","LW":"8"},{"E":"0","LW":"7"},{"E":"1","LW":"6"},{"E":"2","LW":"5"},{"E":"3","LW":"5"},{"E":"4","LW":"4"},{"E":"5","LW":"4"},{"E":"6","LW":"3"},{"E":"7","LW":"3"},{"E":"8","LW":"3"},{"E":"9","LW":"3"},{"E":"10","LW":"2"}],
    "3":  [{"E":"0","LW":"8"},{"E":"0","LW":"7"},{"E":"1","LW":"6"},{"E":"2","LW":"5"},{"E":"3","LW":"5"},{"E":"4","LW":"4"},{"E":"5","LW":"4"},{"E":"6","LW":"3"},{"E":"7","LW":"3"},{"E":"8","LW":"3"},{"E":"9","LW":"2"},{"E":"10","LW":"2"},{"E":"11","LW":"2"}],
    "4":  [{"E":"0","LW":"8"},{"E":"1","LW":"7"},{"E":"2","LW":"6"},{"E":"3","LW":"5"},{"E":"4","LW":"4"},{"E":"5","LW":"4"},{"E":"6","LW":"3"},{"E":"7","LW":"3"},{"E":"8","LW":"2"},{"E":"9","LW":"2"},{"E":"10","LW":"2"},{"E":"11","LW":"2"},{"E":"12","LW":"2"}],
    "5":  [{"E":"1","LW":"7"},{"E":"2","LW":"6"},{"E":"3","LW":"5"},{"E":"4","LW":"4"},{"E":"5","LW":"4"},{"E":"6","LW":"3"},{"E":"7","LW":"2"},{"E":"8","LW":"2"},{"E":"9","LW":"2"},{"E":"10","LW":"2"},{"E":"11","LW":"2"},{"E":"12","LW":"2"},{"E":"14","LW":"1"}],
    "6":  [{"E":"2","LW":"6"},{"E":"3","LW":"6"},{"E":"4","LW":"5"},{"E":"5","LW":"4"},{"E":"6","LW":"3"},{"E":"7","LW":"2"},{"E":"8","LW":"2"},{"E":"9","LW":"2"},{"E":"10","LW":"2"},{"E":"11","LW":"1"},{"E":"12","LW":"1"},{"E":"14","LW":"1"},{"E":"16","LW":"1"}],
    "7":  [{"E":"3","LW":"5"},{"E":"4","LW":"5"},{"E":"5","LW":"4"},{"E":"6","LW":"3"},{"E":"7","LW":"2"},{"E":"8","LW":"2"},{"E":"9","LW":"1"},{"E":"10","LW":"1"},{"E":"11","LW":"1"},{"E":"12","LW":"0"},{"E":"14","LW":"0"},{"E":"16","LW":"0"},{"E":"18","LW":"0"}],
    "8":  [{"E":"4","LW":"4"},{"E":"5","LW":"4"},{"E":"6","LW":"3"},{"E":"7","LW":"2"},{"E":"8","LW":"1"},{"E":"9","LW":"1"},{"E":"10","LW":"0"},{"E":"11","LW":"0"},{"E":"12","LW":"0"},{"E":"14","LW":"0"},{"E":"16","LW":"0"},{"E":"18","LW":"0"},{"E":"K","LW":"0"}],
    "9":  [{"E":"5","LW":"3"},{"E":"6","LW":"3"},{"E":"7","LW":"2"},{"E":"8","LW":"0"},{"E":"9","LW":"0"},{"E":"10","LW":"0"},{"E":"11","LW":"0"},{"E":"12","LW":"0"},{"E":"14","LW":"0"},{"E":"16","LW":"0"},{"E":"18","LW":"0"},{"E":"K","LW":"0"},{"E":"K","LW":"0"}],
    "10": [{"E":"6","LW":"0"},{"E":"7","LW":"0"},{"E":"8","LW":"0"},{"E":"9","LW":"0"},{"E":"10","LW":"0"},{"E":"11","LW":"0"},{"E":"12","LW":"0"},{"E":"14","LW":"0"},{"E":"16","LW":"0"},{"E":"18","LW":"0"},{"E":"K","LW":"0"},{"E":"K","LW":"0"},{"E":"K","LW":"0"}],
}

# Combat ratio column thresholds (lower bound of each column index 0-12)
COMBAT_RATIO_COLUMNS = [-999, -10, -8, -6, -4, -2, 0, 1, 3, 5, 7, 9, 11]

RANDOM_EQUIPMENT_TABLE = [
    {"roll": 1, "item": "Sword", "type": "Weapon"},
    {"roll": 2, "item": "Helmet", "type": "Special Item", "effect": "+2 ENDURANCE"},
    {"roll": 3, "item": "Two Meals", "type": "Backpack Item"},
    {"roll": 4, "item": "Chainmail Waistcoat", "type": "Special Item", "effect": "+4 ENDURANCE"},
    {"roll": 5, "item": "Mace", "type": "Weapon"},
    {"roll": 6, "item": "Healing Potion", "type": "Backpack Item", "effect": "Restores 4 ENDURANCE"},
    {"roll": 7, "item": "Quarterstaff", "type": "Weapon"},
    {"roll": 8, "item": "Spear", "type": "Weapon"},
    {"roll": 9, "item": "12 Gold Crowns", "type": "Currency"},
    {"roll": 0, "item": "Broadsword", "type": "Weapon"},
]

MAGNAKAI_EQUIPMENT_OPTIONS = [
    {"item": "Sword", "type": "Weapon"},
    {"item": "Bow", "type": "Weapon"},
    {"item": "Quiver (6 arrows)", "type": "Special Item"},
    {"item": "Rope", "type": "Backpack Item"},
    {"item": "Potion of Laumspur", "type": "Backpack Item", "effect": "Restores 4 ENDURANCE"},
    {"item": "Lantern", "type": "Backpack Item"},
    {"item": "Mace", "type": "Weapon"},
    {"item": "3 Meals", "type": "Backpack Item"},
]

GRAND_MASTER_EQUIPMENT_OPTIONS = [
    {"item": "Sword", "type": "Weapon"},
    {"item": "Bow", "type": "Weapon"},
    {"item": "Quiver (6 arrows)", "type": "Special Item"},
    {"item": "Dagger", "type": "Weapon"},
    {"item": "Rope", "type": "Backpack Item"},
    {"item": "Potion of Laumspur", "type": "Backpack Item", "effect": "Restores 4 ENDURANCE"},
    {"item": "Lantern", "type": "Backpack Item"},
    {"item": "Mace", "type": "Weapon"},
    {"item": "3 Meals", "type": "Backpack Item"},
]

KAI_RANKS_PATH = os.path.join(os.path.dirname(__file__), "data", "kai_ranks.json")
with open(KAI_RANKS_PATH, "r", encoding="utf-8") as f:
    KAI_RANKS = json.load(f)


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def get_combat_ratio_index(ratio: int) -> int:
    """Return the 0-based column index for the given combat ratio."""
    idx = 0
    for i, threshold in enumerate(COMBAT_RATIO_COLUMNS):
        if ratio >= threshold:
            idx = i
    return idx


def resolve_combat_round(lw_ep: int, enemy_ep: int, ratio: int,
                          use_psi_surge: bool, use_kai_surge: bool,
                          enemy_mindblast: bool, has_mindshield: bool,
                          sommerswerd_vs_undead: bool) -> dict:
    """Simulate one round of combat and return the updated state."""
    roll = random.randint(1, 10)
    col_idx = get_combat_ratio_index(ratio)
    row = COMBAT_RESULTS_TABLE[str(roll)]
    result = row[col_idx]

    e_loss_raw = result["E"]
    lw_loss_raw = result["LW"]

    if e_loss_raw == "K":
        enemy_ep = 0
        e_loss = "K (instant kill)"
    else:
        e_dmg = int(e_loss_raw)
        if sommerswerd_vs_undead:
            e_dmg *= 2
        enemy_ep = max(0, enemy_ep - e_dmg)
        e_loss = str(e_dmg)

    extra_lw_cost = 0
    if use_psi_surge:
        extra_lw_cost += 2
    if use_kai_surge:
        extra_lw_cost += 1
    if enemy_mindblast and not has_mindshield:
        extra_lw_cost += 2

    if lw_loss_raw == "K":
        lw_ep = 0
        lw_loss = "K (instant kill)"
    else:
        lw_dmg = int(lw_loss_raw) + extra_lw_cost
        lw_ep = max(0, lw_ep - lw_dmg)
        lw_loss = str(lw_dmg)

    return {
        "roll": roll,
        "col_idx": col_idx,
        "e_loss": e_loss,
        "lw_loss": lw_loss,
        "lw_ep": lw_ep,
        "enemy_ep": enemy_ep,
        "enemy_dead": enemy_ep <= 0,
        "lw_dead": lw_ep <= 0,
    }


def compute_lore_circle_bonuses(skills: list) -> dict:
    """Return total CS and EP bonuses from completed Magnakai Lore Circles."""
    skills_set = set(skills)
    total_cs = 0
    total_ep = 0
    completed = []
    for circle in MAGNAKAI_LORE_CIRCLES:
        if all(req in skills_set for req in circle["required"]):
            total_cs += circle["cs_bonus"]
            total_ep += circle["ep_bonus"]
            completed.append(circle["name"])
    return {"cs_bonus": total_cs, "ep_bonus": total_ep, "completed_circles": completed}


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/game_data")
def game_data():
    return jsonify({
        "books": GAMEBOOK_METADATA,
        "kai_disciplines": KAI_DISCIPLINES,
        "magnakai_disciplines": MAGNAKAI_DISCIPLINES,
        "magnakai_lore_circles": MAGNAKAI_LORE_CIRCLES,
        "grand_master_disciplines": GRAND_MASTER_DISCIPLINES,
        "new_order_disciplines": NEW_ORDER_DISCIPLINES,
        "magnakai_equipment_options": MAGNAKAI_EQUIPMENT_OPTIONS,
        "grand_master_equipment_options": GRAND_MASTER_EQUIPMENT_OPTIONS,
        "kai_ranks": KAI_RANKS,
    })


@app.route("/api/roll_random")
def roll_random():
    return jsonify({"value": random.randint(0, 9)})


@app.route("/api/roll_equipment")
def roll_equipment():
    """Roll two random items from the Kai starting equipment table."""
    rolls = [random.randint(0, 9), random.randint(0, 9)]
    items = []
    for r in rolls:
        match = next((e for e in RANDOM_EQUIPMENT_TABLE if e["roll"] == r), None)
        if match:
            items.append(match)
    return jsonify({"items": items})


@app.route("/api/combat_round", methods=["POST"])
def combat_round():
    data = request.get_json(force=True)
    try:
        lw_ep = int(data["lw_ep"])
        enemy_ep = int(data["enemy_ep"])
        ratio = int(data["ratio"])
        use_psi_surge = bool(data.get("use_psi_surge", False))
        use_kai_surge = bool(data.get("use_kai_surge", False))
        enemy_mindblast = bool(data.get("enemy_mindblast", False))
        has_mindshield = bool(data.get("has_mindshield", False))
        sommerswerd_vs_undead = bool(data.get("sommerswerd_vs_undead", False))
    except (KeyError, ValueError) as exc:
        return jsonify({"error": str(exc)}), 400

    result = resolve_combat_round(
        lw_ep, enemy_ep, ratio,
        use_psi_surge, use_kai_surge,
        enemy_mindblast, has_mindshield,
        sommerswerd_vs_undead,
    )
    return jsonify(result)


@app.route("/api/lore_circles", methods=["POST"])
def lore_circles():
    data = request.get_json(force=True)
    skills = data.get("skills", [])
    return jsonify(compute_lore_circle_bonuses(skills))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
