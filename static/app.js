const state = {
  max_cs: 15,
  current_cs: 15,
  max_ep: 25,
  current_ep: 25,
  inventory: {
    backpack_items: [],
    weapons: [],
    special_items: [],
    meals: 0,
    gold_crowns: 0,
    quivers: []
  },
  notes: [],
  current_skills_list: [],
  weapon_masteries: {
    Weaponskill: "",
    Weaponmastery: "",
    "Grand Weaponmastery": ""
  },
  combat: {
    active: false,
    status: "Idle",
    enemy_ep: 0,
    rounds: 0,
    allow_evade_after: 0,
    settings: null,
    log: []
  }
};

let bootstrapData = null;

const $ = (id) => document.getElementById(id);

function showToast(message, isError = false) {
  const toast = $("toast");
  toast.textContent = message;
  toast.classList.remove("hidden", "error");
  if (isError) toast.classList.add("error");
  setTimeout(() => toast.classList.add("hidden"), 2500);
}

function parseIntSafe(value, fallback = 0) {
  const parsed = Number.parseInt(value, 10);
  return Number.isNaN(parsed) ? fallback : parsed;
}

function getAllSkills() {
  if (!bootstrapData) return [];
  const skills = bootstrapData.kai_skills;
  return [
    ...skills.kai_disciplines,
    ...skills.magnakai_disciplines,
    ...skills.grand_master_disciplines,
    ...skills.new_order_grand_master_disciplines
  ];
}

function calculateLoreBonuses() {
  let bonusCS = 0;
  let bonusEP = 0;
  const active = [];
  const circles = bootstrapData.kai_skills.magnakai_lore_circles;
  circles.forEach((circle) => {
    const unlocked = circle.required_disciplines.every((skill) => state.current_skills_list.includes(skill));
    if (unlocked) {
      bonusCS += circle.bonus_cs;
      bonusEP += circle.bonus_ep;
      active.push(circle);
    }
  });
  return { bonusCS, bonusEP, active };
}

function resolveTierRank(table, skillsLearned) {
  if (!Array.isArray(table) || skillsLearned <= 0) return "Unranked";

  const sorted = table
    .filter((entry) => entry && Number.isFinite(entry.skills_learned) && typeof entry.rank === "string")
    .slice()
    .sort((a, b) => a.skills_learned - b.skills_learned);

  if (!sorted.length) return "Unranked";

  let selected = sorted[0].rank;
  sorted.forEach((entry) => {
    if (skillsLearned >= entry.skills_learned) {
      selected = entry.rank;
    }
  });
  return selected;
}

function calculateCurrentRank() {
  if (!bootstrapData) return "Unranked";

  const skills = bootstrapData.kai_skills;
  const ranks = bootstrapData.kai_ranks || {};

  const kaiCount = state.current_skills_list.filter((skill) => skills.kai_disciplines.includes(skill)).length;
  const magnakaiCount = state.current_skills_list
    .filter((skill) => skills.magnakai_disciplines.includes(skill)).length;
  const grandMasterCount = state.current_skills_list
    .filter((skill) => skills.grand_master_disciplines.includes(skill)).length;

  if (grandMasterCount > 0) {
    return resolveTierRank(ranks.grand_master_disciplines, grandMasterCount);
  }
  if (magnakaiCount > 0) {
    return resolveTierRank(ranks.magnakai_disciplines, magnakaiCount);
  }
  if (kaiCount > 0) {
    return resolveTierRank(ranks.kai_disciplines, kaiCount);
  }

  return "Unranked";
}

function getEffectiveMaxes() {
  const lore = calculateLoreBonuses();
  return {
    effectiveCS: state.max_cs + lore.bonusCS,
    effectiveEP: state.max_ep + lore.bonusEP
  };
}

function clampCurrentStats() {
  const { effectiveCS, effectiveEP } = getEffectiveMaxes();
  state.current_cs = Math.max(0, Math.min(state.current_cs, effectiveCS));
  state.current_ep = Math.max(0, Math.min(state.current_ep, effectiveEP));
}

function renderStats() {
  clampCurrentStats();
  const { effectiveCS, effectiveEP } = getEffectiveMaxes();
  $("max-cs").value = state.max_cs;
  $("current-cs").value = state.current_cs;
  $("max-ep").value = state.max_ep;
  $("current-ep").value = state.current_ep;
  $("effective-cs").textContent = effectiveCS;
  $("effective-ep").textContent = effectiveEP;

  const circles = calculateLoreBonuses().active;
  const activeCirclesList = $("active-circles");
  activeCirclesList.innerHTML = "";
  if (!circles.length) {
    const li = document.createElement("li");
    li.textContent = "No lore circles active.";
    activeCirclesList.appendChild(li);
  } else {
    circles.forEach((circle) => {
      const li = document.createElement("li");
      li.textContent = `${circle.name} (+${circle.bonus_cs} CS, +${circle.bonus_ep} EP)`;
      activeCirclesList.appendChild(li);
    });
  }
}

function renderSkills() {
  const currentList = $("current-skills");
  currentList.innerHTML = "";
  state.current_skills_list.slice().sort().forEach((skill) => {
    const li = document.createElement("li");
    li.className = "pill";
    li.textContent = skill;
    const btn = document.createElement("button");
    btn.textContent = "Remove";
    btn.addEventListener("click", () => {
      state.current_skills_list = state.current_skills_list.filter((s) => s !== skill);
      renderAll();
    });
    li.appendChild(btn);
    currentList.appendChild(li);
  });

  $("weaponskill-weapon").value = state.weapon_masteries.Weaponskill;
  $("weaponmastery-weapon").value = state.weapon_masteries.Weaponmastery;
  $("grandweaponmastery-weapon").value = state.weapon_masteries["Grand Weaponmastery"];
  $("rank-display").textContent = calculateCurrentRank();
}

function inventoryCount() {
  return state.inventory.backpack_items.length + state.inventory.meals;
}

function renderListWithRemove(targetId, list, removeFn) {
  const target = $(targetId);
  target.innerHTML = "";
  list.forEach((entry, index) => {
    const li = document.createElement("li");
    if (typeof entry === "string") {
      li.textContent = entry;
    } else {
      li.textContent = `${entry.name} (${entry.arrows}/6 arrows)`;
    }
    const button = document.createElement("button");
    button.textContent = "Remove";
    button.addEventListener("click", () => removeFn(index));
    li.appendChild(button);
    target.appendChild(li);
  });
}

function renderInventory() {
  $("meals-input").value = state.inventory.meals;
  $("gold-input").value = state.inventory.gold_crowns;
  renderListWithRemove("backpack-list", state.inventory.backpack_items, (index) => {
    state.inventory.backpack_items.splice(index, 1);
    renderAll();
  });
  renderListWithRemove("weapons-list", state.inventory.weapons, (index) => {
    state.inventory.weapons.splice(index, 1);
    renderAll();
  });
  renderListWithRemove("special-items-list", state.inventory.special_items, (index) => {
    state.inventory.special_items.splice(index, 1);
    renderAll();
  });
  renderListWithRemove("quivers-list", state.inventory.quivers, (index) => {
    state.inventory.quivers.splice(index, 1);
    renderAll();
  });
}

function renderNotes() {
  const noteList = $("notes-list");
  noteList.innerHTML = "";
  state.notes.forEach((note, index) => {
    const li = document.createElement("li");
    li.textContent = `Book ${note.book_number}: ${note.text}`;
    const button = document.createElement("button");
    button.textContent = "Remove";
    button.addEventListener("click", () => {
      state.notes.splice(index, 1);
      renderAll();
    });
    li.appendChild(button);
    noteList.appendChild(li);
  });
}

function renderCombat() {
  $("combat-status").textContent = state.combat.status;
  $("combat-enemy-ep").textContent = state.combat.active ? state.combat.enemy_ep : "-";
  $("combat-rounds").textContent = String(state.combat.rounds);

  const nextRound = $("next-round");
  const evade = $("evade");
  nextRound.disabled = !state.combat.active;
  evade.disabled = !state.combat.active || state.combat.rounds < state.combat.allow_evade_after;

  const log = $("combat-log");
  log.innerHTML = "";
  state.combat.log.slice().reverse().forEach((entry) => {
    const li = document.createElement("li");
    li.textContent = entry;
    log.appendChild(li);
  });
}

function renderWeaponOptions() {
  const weaponSelect = $("wielded-weapon");
  weaponSelect.innerHTML = "";
  const unarmed = document.createElement("option");
  unarmed.value = "";
  unarmed.textContent = "Unarmed";
  weaponSelect.appendChild(unarmed);

  state.inventory.weapons.forEach((weapon) => {
    const option = document.createElement("option");
    option.value = weapon;
    option.textContent = weapon;
    weaponSelect.appendChild(option);
  });
}

function renderMentalDisciplineOptions() {
  const select = $("mental-discipline");
  const choices = ["None"];
  ["Mindblast", "Psi-surge", "Kai-surge"].forEach((skill) => {
    if (state.current_skills_list.includes(skill)) choices.push(skill);
  });
  select.innerHTML = "";
  choices.forEach((choice) => {
    const option = document.createElement("option");
    option.value = choice === "None" ? "" : choice;
    option.textContent = choice;
    select.appendChild(option);
  });
}

function renderAll() {
  renderStats();
  renderSkills();
  renderInventory();
  renderNotes();
  renderWeaponOptions();
  renderMentalDisciplineOptions();
  renderCombat();
}

function ratioToColumnIndex(ratio) {
  if (ratio <= -11) return 0;
  if (ratio <= -9) return 1;
  if (ratio <= -7) return 2;
  if (ratio <= -5) return 3;
  if (ratio <= -3) return 4;
  if (ratio <= -1) return 5;
  if (ratio === 0) return 6;
  if (ratio <= 2) return 7;
  if (ratio <= 4) return 8;
  if (ratio <= 6) return 9;
  if (ratio <= 8) return 10;
  if (ratio <= 10) return 11;
  return 12;
}

function parseLoss(value, target, source) {
  if (value === "K") return source === "enemy" ? target : target;
  return parseIntSafe(value, 0);
}

function hasPsychicDefense() {
  return state.current_skills_list.includes("Mindshield") ||
    state.current_skills_list.includes("Psi-screen") ||
    state.current_skills_list.includes("Kai-screen");
}

function computeCombatModifier(settings) {
  let ecs = state.current_cs;
  let notes = [];

  const wielded = settings.wielded_weapon;
  if (!wielded) {
    ecs -= 4;
    notes.push("Unarmed penalty -4 CS");
  } else if (wielded.toLowerCase().includes("sommerswerd")) {
    ecs += 8;
    notes.push("Sommerswerd +8 CS");
  } else {
    if (state.current_skills_list.includes("Grand Weaponmastery") &&
        state.weapon_masteries["Grand Weaponmastery"].trim().toLowerCase() === wielded.toLowerCase()) {
      ecs += 4;
      notes.push("Grand Weaponmastery +4 CS");
    } else if (state.current_skills_list.includes("Weaponmastery") &&
        state.weapon_masteries.Weaponmastery.trim().toLowerCase() === wielded.toLowerCase()) {
      ecs += 3;
      notes.push("Weaponmastery +3 CS");
    } else if (state.current_skills_list.includes("Weaponskill") &&
        state.weapon_masteries.Weaponskill.trim().toLowerCase() === wielded.toLowerCase()) {
      ecs += 2;
      notes.push("Weaponskill +2 CS");
    }
  }

  if (settings.using_shield && wielded) {
    ecs += 2;
    notes.push("Shield +2 CS");
  }
  if (settings.wearing_silver_helm) {
    ecs += 2;
    notes.push("Silver Helm +2 CS");
  }

  if (settings.mental_discipline === "Mindblast" && !settings.enemy_psychic_immune) {
    ecs += 2;
    notes.push("Mindblast +2 CS");
  }
  if (settings.mental_discipline === "Psi-surge") {
    ecs += 4;
    notes.push("Psi-surge +4 CS");
  }
  if (settings.mental_discipline === "Kai-surge") {
    ecs += 8;
    notes.push("Kai-surge +8 CS");
  }

  return { ecs, notes };
}

function startCombat() {
  if (state.current_ep <= 0) {
    showToast("Current Endurance must be above 0 to start combat.", true);
    return;
  }

  const settings = {
    enemy_cs: parseIntSafe($("enemy-cs").value, 0),
    enemy_ep: parseIntSafe($("enemy-ep").value, 1),
    enemy_cs_mod: parseIntSafe($("enemy-cs-mod").value, 0),
    allow_evade_after: parseIntSafe($("evade-after").value, 0),
    enemy_psychic_attack: $("enemy-psychic-attack").checked,
    enemy_psychic_immune: $("enemy-psychic-immune").checked,
    enemy_undead: $("enemy-undead").checked,
    using_shield: $("using-shield").checked,
    wearing_silver_helm: $("wearing-silver-helm").checked,
    wearing_chainmail: $("wearing-chainmail").checked,
    wielded_weapon: $("wielded-weapon").value,
    mental_discipline: $("mental-discipline").value
  };

  state.combat.active = true;
  state.combat.status = "In Progress";
  state.combat.enemy_ep = settings.enemy_ep;
  state.combat.rounds = 0;
  state.combat.allow_evade_after = settings.allow_evade_after;
  state.combat.settings = settings;
  state.combat.log = ["Combat started."];
  renderAll();
}

function runRound() {
  if (!state.combat.active) return;

  const settings = state.combat.settings;
  const chainmailBonus = settings.wearing_chainmail ? 4 : 0;
  const effectiveMaxEP = getEffectiveMaxes().effectiveEP + chainmailBonus;

  const { ecs, notes } = computeCombatModifier(settings);
  const enemyEcs = settings.enemy_cs + settings.enemy_cs_mod;
  const ratio = ecs - enemyEcs;
  const colIndex = ratioToColumnIndex(ratio);
  const roll = Math.floor(Math.random() * 10) + 1;
  const entry = bootstrapData.combat.results_by_roll[String(roll)][colIndex];

  let enemyLoss = entry.E === "K" ? state.combat.enemy_ep : parseIntSafe(entry.E, 0);
  let lwLoss = entry.LW === "K" ? state.current_ep : parseIntSafe(entry.LW, 0);

  if (settings.enemy_undead && settings.wielded_weapon.toLowerCase().includes("sommerswerd")) {
    enemyLoss *= 2;
    notes.push("Sommerswerd vs undead: enemy damage doubled");
  }

  if (settings.mental_discipline === "Psi-surge") {
    lwLoss += 2;
    notes.push("Psi-surge cost: +2 LW EP loss");
  }
  if (settings.mental_discipline === "Kai-surge") {
    lwLoss += 1;
    notes.push("Kai-surge cost: +1 LW EP loss");
  }

  if (settings.enemy_psychic_attack && !hasPsychicDefense()) {
    lwLoss += 2;
    notes.push("Enemy Mindblast: +2 LW EP loss");
  }

  state.combat.rounds += 1;
  state.combat.enemy_ep = Math.max(0, state.combat.enemy_ep - enemyLoss);
  state.current_ep = Math.max(0, state.current_ep - lwLoss);
  state.current_ep = Math.min(state.current_ep, effectiveMaxEP);

  const line = `Round ${state.combat.rounds} | Roll ${roll} | CR ${ratio} | Enemy -${enemyLoss} EP | Lone Wolf -${lwLoss} EP`;
  const detail = notes.length ? ` (${notes.join(", ")})` : "";
  state.combat.log.push(line + detail);

  if (state.combat.enemy_ep <= 0) {
    state.combat.status = "Victory";
    state.combat.active = false;
    state.combat.log.push("Enemy defeated.");
  } else if (state.current_ep <= 0) {
    state.combat.status = "Defeat";
    state.combat.active = false;
    state.combat.log.push("Lone Wolf has fallen.");
  }

  renderAll();
}

function evadeCombat() {
  if (!state.combat.active) return;
  if (state.combat.rounds < state.combat.allow_evade_after) {
    showToast("You cannot evade yet.", true);
    return;
  }
  state.combat.active = false;
  state.combat.status = "Evaded";
  state.combat.log.push("Combat evaded.");
  renderAll();
}

function wireEvents() {
  ["max-cs", "current-cs", "max-ep", "current-ep"].forEach((id) => {
    $(id).addEventListener("change", () => {
      state.max_cs = Math.max(0, parseIntSafe($("max-cs").value, 0));
      state.current_cs = Math.max(0, parseIntSafe($("current-cs").value, 0));
      state.max_ep = Math.max(0, parseIntSafe($("max-ep").value, 0));
      state.current_ep = Math.max(0, parseIntSafe($("current-ep").value, 0));
      renderAll();
    });
  });

  $("add-skill").addEventListener("click", () => {
    const selected = $("skill-select").value;
    if (!selected) return;
    if (!state.current_skills_list.includes(selected)) {
      state.current_skills_list.push(selected);
      renderAll();
    }
  });

  $("weaponskill-weapon").addEventListener("change", (e) => {
    state.weapon_masteries.Weaponskill = e.target.value.trim();
  });
  $("weaponmastery-weapon").addEventListener("change", (e) => {
    state.weapon_masteries.Weaponmastery = e.target.value.trim();
  });
  $("grandweaponmastery-weapon").addEventListener("change", (e) => {
    state.weapon_masteries["Grand Weaponmastery"] = e.target.value.trim();
  });

  $("add-backpack-item").addEventListener("click", () => {
    const item = $("backpack-item-input").value.trim();
    if (!item) return;
    if (inventoryCount() >= 8) {
      showToast("Backpack limit reached.", true);
      return;
    }
    state.inventory.backpack_items.push(item);
    $("backpack-item-input").value = "";
    renderAll();
  });

  $("add-weapon").addEventListener("click", () => {
    const weapon = $("weapon-input").value.trim();
    if (!weapon) return;
    if (state.inventory.weapons.length >= 2) {
      showToast("Weapon limit reached.", true);
      return;
    }
    state.inventory.weapons.push(weapon);
    $("weapon-input").value = "";
    renderAll();
  });

  $("add-special-item").addEventListener("click", () => {
    const item = $("special-item-input").value.trim();
    if (!item) return;
    if (state.inventory.special_items.length >= 12) {
      showToast("Special item limit reached.", true);
      return;
    }
    state.inventory.special_items.push(item);
    $("special-item-input").value = "";
    renderAll();
  });

  $("meals-input").addEventListener("change", () => {
    const meals = Math.max(0, parseIntSafe($("meals-input").value, 0));
    if (meals + state.inventory.backpack_items.length > 8) {
      showToast("Meals plus backpack items cannot exceed 8.", true);
      $("meals-input").value = state.inventory.meals;
      return;
    }
    state.inventory.meals = meals;
    renderAll();
  });

  $("gold-input").addEventListener("change", () => {
    state.inventory.gold_crowns = Math.max(0, Math.min(50, parseIntSafe($("gold-input").value, 0)));
    renderAll();
  });

  $("add-quiver").addEventListener("click", () => {
    const name = $("quiver-name").value.trim() || `Quiver ${state.inventory.quivers.length + 1}`;
    const arrows = Math.max(0, Math.min(6, parseIntSafe($("quiver-arrows").value, 6)));
    state.inventory.quivers.push({ name, arrows });
    $("quiver-name").value = "";
    $("quiver-arrows").value = "6";
    renderAll();
  });

  $("add-note").addEventListener("click", () => {
    const bookNumber = parseIntSafe($("note-book").value, 1);
    const text = $("note-text").value.trim();
    if (!text) return;
    state.notes.push({ book_number: bookNumber, text });
    $("note-text").value = "";
    renderAll();
  });

  $("start-combat").addEventListener("click", startCombat);
  $("next-round").addEventListener("click", runRound);
  $("evade").addEventListener("click", evadeCombat);

  $("save-game").addEventListener("click", saveGame);
  $("refresh-saves").addEventListener("click", refreshSaves);

  $("close-modal").addEventListener("click", () => {
    $("modal").classList.add("hidden");
  });
}

function fillSelectors() {
  const books = bootstrapData.gamebook_metadata;
  const noteBook = $("note-book");
  const saveBook = $("save-book");
  noteBook.innerHTML = "";
  saveBook.innerHTML = "";
  books.forEach((book) => {
    const label = `${book.book_number} - ${book.book_name}`;
    const opt1 = document.createElement("option");
    opt1.value = String(book.book_number);
    opt1.textContent = label;
    noteBook.appendChild(opt1);

    const opt2 = document.createElement("option");
    opt2.value = String(book.book_number);
    opt2.textContent = label;
    saveBook.appendChild(opt2);
  });

  const skillSelect = $("skill-select");
  skillSelect.innerHTML = "";
  getAllSkills().sort().forEach((skill) => {
    const option = document.createElement("option");
    option.value = skill;
    option.textContent = skill;
    skillSelect.appendChild(option);
  });
}

async function saveGame() {
  const sessionName = $("save-session").value.trim();
  if (!sessionName) {
    showToast("Session name is required.", true);
    return;
  }

  const payload = {
    session_name: sessionName,
    book_number: parseIntSafe($("save-book").value, 1),
    page_number: parseIntSafe($("save-page").value, 1),
    created_at: new Date().toISOString(),
    state
  };

  const response = await fetch("/api/save", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const data = await response.json();
  if (!response.ok) {
    showToast(data.error || "Save failed", true);
    return;
  }

  showToast(`Saved: ${data.save_name}`);
  refreshSaves();
}

async function refreshSaves() {
  const response = await fetch("/api/saves");
  const data = await response.json();
  const saveList = $("save-list");
  saveList.innerHTML = "";
  data.saves.forEach((save) => {
    const li = document.createElement("li");
    li.textContent = `${save.save_name}`;
    const button = document.createElement("button");
    button.textContent = "Load";
    button.addEventListener("click", () => loadGame(save.filename));
    li.appendChild(button);
    saveList.appendChild(li);
  });
}

function deepAssign(target, source) {
  Object.keys(target).forEach((key) => {
    if (source[key] === undefined) return;
    if (target[key] && typeof target[key] === "object" && !Array.isArray(target[key])) {
      deepAssign(target[key], source[key]);
    } else {
      target[key] = source[key];
    }
  });
}

async function loadGame(filename) {
  const response = await fetch("/api/load", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ filename })
  });
  const data = await response.json();
  if (!response.ok) {
    showToast(data.error || "Load failed", true);
    return;
  }

  deepAssign(state, data.state);
  renderAll();

  $("modal-text").textContent = `Resume at Book ${data.book_number} (${data.book_name}), page ${data.page_number}.`;
  $("modal").classList.remove("hidden");
  showToast("Save loaded.");
}

async function init() {
  const response = await fetch("/api/bootstrap");
  bootstrapData = await response.json();
  fillSelectors();
  wireEvents();
  renderAll();
  refreshSaves();
}

init();
