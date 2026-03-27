# Lone Wolf Gamebook Assistant App

## General Application Instructions
- Built in Python 3
- Runs as a web application
- Should be responsive - should render on a large screen, but equally work for a phone screen using touch
- App must have a setup script in both bash and powershell that sets up the python venv if not preent and installs all requirements from requirements.txt
- App must have a run script in both bash and powershell that activates the venv and runs the applcation
- All requirements must be saved to requirements.txt

## Inventory_Rules
- Backpack Items: You can carry a maximum of 8 items in your backpack (e.g., meals, potions, ropes).
- Weapons: You can carry a maximum of 2 weapons at any given time (e.g., a sword and a mace).
- Gold Crowns: Your belt pouch can hold a maximum of 50 Gold Crowns.
- Special Items: Originally uncapped in the very first books, creator Joe Dever later introduced an official limit starting around book 8 (The Jungle of Horrors). Under this rule, you can carry a maximum of 12 Special Items (e.g., the Crystal Star Pendant, a map, or the Sommerswerd). Any additional Special Items must be left in safekeeping at the Kai Monastery.
- Quivers: A standard quiver holds up to 6 arrows, and you can carry multiple quivers if you find or buy them.


## Combat_Results_Table

```JSON
{
  "combat_results_table": {
    "description": "Values represent the Endurance Point loss for the Enemy (E) and Lone Wolf (LW). 'K' indicates an instant kill.",
    "columns_combat_ratio": [
      "≤ -11", "-10 to -9", "-8 to -7", "-6 to -5", "-4 to -3", "-2 to -1", "0", "+1 to +2", "+3 to +4", "+5 to +6", "+7 to +8", "+9 to +10", "≥ +11"
    ],
    "results_by_roll": {
      "1": [
        {"E": "0", "LW": "K"}, {"E": "0", "LW": "K"}, {"E": "0", "LW": "8"}, {"E": "0", "LW": "6"}, {"E": "1", "LW": "6"}, {"E": "2", "LW": "5"}, {"E": "3", "LW": "5"}, {"E": "4", "LW": "5"}, {"E": "5", "LW": "4"}, {"E": "6", "LW": "4"}, {"E": "7", "LW": "4"}, {"E": "8", "LW": "3"}, {"E": "9", "LW": "3"}
      ],
      "2": [
        {"E": "0", "LW": "K"}, {"E": "0", "LW": "8"}, {"E": "0", "LW": "7"}, {"E": "1", "LW": "6"}, {"E": "2", "LW": "5"}, {"E": "3", "LW": "5"}, {"E": "4", "LW": "4"}, {"E": "5", "LW": "4"}, {"E": "6", "LW": "3"}, {"E": "7", "LW": "3"}, {"E": "8", "LW": "3"}, {"E": "9", "LW": "3"}, {"E": "10", "LW": "2"}
      ],
      "3": [
        {"E": "0", "LW": "8"}, {"E": "0", "LW": "7"}, {"E": "1", "LW": "6"}, {"E": "2", "LW": "5"}, {"E": "3", "LW": "5"}, {"E": "4", "LW": "4"}, {"E": "5", "LW": "4"}, {"E": "6", "LW": "3"}, {"E": "7", "LW": "3"}, {"E": "8", "LW": "3"}, {"E": "9", "LW": "2"}, {"E": "10", "LW": "2"}, {"E": "11", "LW": "2"}
      ],
      "4": [
        {"E": "0", "LW": "8"}, {"E": "1", "LW": "7"}, {"E": "2", "LW": "6"}, {"E": "3", "LW": "5"}, {"E": "4", "LW": "4"}, {"E": "5", "LW": "4"}, {"E": "6", "LW": "3"}, {"E": "7", "LW": "3"}, {"E": "8", "LW": "2"}, {"E": "9", "LW": "2"}, {"E": "10", "LW": "2"}, {"E": "11", "LW": "2"}, {"E": "12", "LW": "2"}
      ],
      "5": [
        {"E": "1", "LW": "7"}, {"E": "2", "LW": "6"}, {"E": "3", "LW": "5"}, {"E": "4", "LW": "4"}, {"E": "5", "LW": "4"}, {"E": "6", "LW": "3"}, {"E": "7", "LW": "2"}, {"E": "8", "LW": "2"}, {"E": "9", "LW": "2"}, {"E": "10", "LW": "2"}, {"E": "11", "LW": "2"}, {"E": "12", "LW": "2"}, {"E": "14", "LW": "1"}
      ],
      "6": [
        {"E": "2", "LW": "6"}, {"E": "3", "LW": "6"}, {"E": "4", "LW": "5"}, {"E": "5", "LW": "4"}, {"E": "6", "LW": "3"}, {"E": "7", "LW": "2"}, {"E": "8", "LW": "2"}, {"E": "9", "LW": "2"}, {"E": "10", "LW": "2"}, {"E": "11", "LW": "1"}, {"E": "12", "LW": "1"}, {"E": "14", "LW": "1"}, {"E": "16", "LW": "1"}
      ],
      "7": [
        {"E": "3", "LW": "5"}, {"E": "4", "LW": "5"}, {"E": "5", "LW": "4"}, {"E": "6", "LW": "3"}, {"E": "7", "LW": "2"}, {"E": "8", "LW": "2"}, {"E": "9", "LW": "1"}, {"E": "10", "LW": "1"}, {"E": "11", "LW": "1"}, {"E": "12", "LW": "0"}, {"E": "14", "LW": "0"}, {"E": "16", "LW": "0"}, {"E": "18", "LW": "0"}
      ],
      "8": [
        {"E": "4", "LW": "4"}, {"E": "5", "LW": "4"}, {"E": "6", "LW": "3"}, {"E": "7", "LW": "2"}, {"E": "8", "LW": "1"}, {"E": "9", "LW": "1"}, {"E": "10", "LW": "0"}, {"E": "11", "LW": "0"}, {"E": "12", "LW": "0"}, {"E": "14", "LW": "0"}, {"E": "16", "LW": "0"}, {"E": "18", "LW": "0"}, {"E": "K", "LW": "0"}
      ],
      "9": [
        {"E": "5", "LW": "3"}, {"E": "6", "LW": "3"}, {"E": "7", "LW": "2"}, {"E": "8", "LW": "0"}, {"E": "9", "LW": "0"}, {"E": "10", "LW": "0"}, {"E": "11", "LW": "0"}, {"E": "12", "LW": "0"}, {"E": "14", "LW": "0"}, {"E": "16", "LW": "0"}, {"E": "18", "LW": "0"}, {"E": "K", "LW": "0"}, {"E": "K", "LW": "0"}
      ],
      "10": [
        {"E": "6", "LW": "0"}, {"E": "7", "LW": "0"}, {"E": "8", "LW": "0"}, {"E": "9", "LW": "0"}, {"E": "10", "LW": "0"}, {"E": "11", "LW": "0"}, {"E": "12", "LW": "0"}, {"E": "14", "LW": "0"}, {"E": "16", "LW": "0"}, {"E": "18", "LW": "0"}, {"E": "K", "LW": "0"}, {"E": "K", "LW": "0"}, {"E": "K", "LW": "0"}
      ]
    }
  }
}
```

## Combat_Algorithm
### Phase 1: Pre-Combat Initialization
1. Determine Base Stats
- Retrieve Lone Wolf’s current Combat Skill (CS) and Endurance Points (EP).
- Enter the Enemy’s CS and EP

2. Calculate Lone Wolf's Effective Combat Skill (ECS)
- Apply modifiers to Lone Wolf's base CS in the following order:
    - Weapon Check: * If Lone Wolf has no weapons, apply a -4 CS penalty (fighting unarmed).
        - If wielding a standard weapon with the relevant Weaponskill (Kai) / Weaponmastery (Magnakai) / Grand Weaponmastery (Grand Master) discipline, apply the corresponding bonus (+2, +3, or +4 CS).
        - Special Weapons (e.g., The Sommerswerd): If wielding the Sommerswerd, apply +8 CS. (Note: This does not stack with standard Weaponskill bonuses unless specifically stated by your tier rules).

    - Special Items:
        - If carrying a Shield and fighting one-handed, apply +2 CS.
        - Apply bonuses from specific armor (e.g., Silver Helm +2 CS, Chainmail +4 EP max).
    - Mental Disciplines (Choose one per combat, if applicable):
        - Mindblast: Apply +2 CS (unless the enemy is immune to psychic attacks).
        - Psi-surge: Apply +4 CS (costs 2 EP per round of use; enemy cannot be immune).
        - Kai-surge: Apply +8 CS (costs 1 EP per round of use).
        - Allow the user to optionally toggle one of these to use in this combat round. The toggle list should only show the skills if they have been added to the user's `current_skills_list`

3. Calculate the Enemy's Effective Combat Skill
- Base Enemy CS.
- Add any situational bonuses dictated by the specific book paragraph (e.g., surprise attacks, darkness).
- Mindblast Penalty: If the enemy uses Mindblast and Lone Wolf does not have the Mind Shield / Psi-screen discipline, Lone Wolf loses 2 EP per round (this does not affect the CS ratio, but affects the EP pool).

4. Calculate the Combat Ratio (CR)
- Subtract the Enemy's Effective CS from Lone Wolf's Effective CS.
- Formula: Combat Ratio = (Lone Wolf ECS) - (Enemy ECS)

### Phase 2: Combat Round Loop
Execute this loop until either Lone Wolf or the Enemy reaches 0 Endurance Points, or until the text allows Lone Wolf to evade.
1. Generate a Random Number
- Pick a number from 1 to 10

2. Cross-Reference the combat_results_table
- Find the entry in `combat_results_table.results_by_row` that matches the Random Number (1-10).
- Find the array entry matching the calculated Combat Ratio (CR) based on the headings in `combat_results_table.columns_combat_ratio`.
- The intersection gives the EP loss for both the Enemy (E) and Lone Wolf (LW). A result of "K" means an instant kill.

3. Apply Special Multipliers / Deductions
- Undead Multiplier: If wielding the Sommerswerd against an undead enemy, multiply the Enemy's EP loss by 2.
- Psi-surge Cost: If using Psi-surge, deduct an additional 2 EP from Lone Wolf.
- Enemy Mindblast: If the enemy has Mindblast and Lone Wolf lacks Mind Shield, deduct an additional 2 EP from Lone Wolf.

4. Update Endurance Points
- Subtract the final EP loss from both Lone Wolf and the Enemy.

5. Check for Termination
- If Enemy EP is 0 or less: Victory. Proceed to the post-combat text.
- If Lone Wolf EP is 0 or less: Defeat. The adventure ends.
- If the text allows for Evasion (e.g., "You may evade after 3 rounds of combat"): You may choose to exit the loop and turn to the designated evasion paragraph.

Phase 3: Post-Combat Resolution
- Healing: If Lone Wolf has the Healing or Curing discipline, and his EP is below maximum, he regains 1 EP for every section of the book traversed without combat. (Note: Healing does not occur during the combat loop).
- Loot: Collect any dropped Gold Crowns, weapons, or special items, ensuring you do not exceed the inventory limits (2 weapons, 8 backpack items, 50 Gold Crowns).


## Gamebook_Metadata
```json
[
  {
    "book_number": 1,
    "book_name": "Flight from the Dark",
    "subseries": "Kai"
  },
  {
    "book_number": 2,
    "book_name": "Fire on the Water",
    "subseries": "Kai"
  },
  {
    "book_number": 3,
    "book_name": "The Caverns of Kalte",
    "subseries": "Kai"
  },
  {
    "book_number": 4,
    "book_name": "The Chasm of Doom",
    "subseries": "Kai"
  },
  {
    "book_number": 5,
    "book_name": "Shadow on the Sand",
    "subseries": "Kai"
  },
  {
    "book_number": 6,
    "book_name": "The Kingdoms of Terror",
    "subseries": "Magnakai"
  },
  {
    "book_number": 7,
    "book_name": "Castle Death",
    "subseries": "Magnakai"
  },
  {
    "book_number": 8,
    "book_name": "The Jungle of Horrors",
    "subseries": "Magnakai"
  },
  {
    "book_number": 9,
    "book_name": "The Cauldron of Fear",
    "subseries": "Magnakai"
  },
  {
    "book_number": 10,
    "book_name": "The Dungeons of Torgar",
    "subseries": "Magnakai"
  },
  {
    "book_number": 11,
    "book_name": "The Prisoners of Time",
    "subseries": "Magnakai"
  },
  {
    "book_number": 12,
    "book_name": "The Masters of Darkness",
    "subseries": "Magnakai"
  },
  {
    "book_number": 13,
    "book_name": "The Plague Lords of Ruel",
    "subseries": "Grand Master"
  },
  {
    "book_number": 14,
    "book_name": "The Captives of Kaag",
    "subseries": "Grand Master"
  },
  {
    "book_number": 15,
    "book_name": "The Darke Crusade",
    "subseries": "Grand Master"
  },
  {
    "book_number": 16,
    "book_name": "The Legacy of Vashna",
    "subseries": "Grand Master"
  },
  {
    "book_number": 17,
    "book_name": "The Deathlord of Ixia",
    "subseries": "Grand Master"
  },
  {
    "book_number": 18,
    "book_name": "Dawn of the Dragons",
    "subseries": "Grand Master"
  },
  {
    "book_number": 19,
    "book_name": "Wolf's Bane",
    "subseries": "Grand Master"
  },
  {
    "book_number": 20,
    "book_name": "The Curse of Naar",
    "subseries": "Grand Master"
  },
  {
    "book_number": 21,
    "book_name": "Voyage of the Moonstone",
    "subseries": "New Order"
  },
  {
    "book_number": 22,
    "book_name": "The Buccaneers of Shadaki",
    "subseries": "New Order"
  },
  {
    "book_number": 23,
    "book_name": "Mydnight's Hero",
    "subseries": "New Order"
  },
  {
    "book_number": 24,
    "book_name": "Rune War",
    "subseries": "New Order"
  },
  {
    "book_number": 25,
    "book_name": "Trail of the Wolf",
    "subseries": "New Order"
  },
  {
    "book_number": 26,
    "book_name": "The Fall of Blood Mountain",
    "subseries": "New Order"
  },
  {
    "book_number": 27,
    "book_name": "Vampirium",
    "subseries": "New Order"
  },
  {
    "book_number": 28,
    "book_name": "The Hunger of Sejanoz",
    "subseries": "New Order"
  },
  {
    "book_number": 29,
    "book_name": "The Storms of Chai",
    "subseries": "New Order"
  },
  {
    "book_number": 30,
    "book_name": "Dead in the Deep",
    "subseries": "New Order"
  },
  {
    "book_number": 31,
    "book_name": "The Dusk of Eternal Night",
    "subseries": "New Order"
  },
  {
    "book_number": 32,
    "book_name": "Light of the Kai",
    "subseries": "New Order"
  }
]
```

## Kai_Skills
```JSON
{
  "lone_wolf_skills": {
    "kai_disciplines": [
      {
        "name": "Camouflage",
        "description": "The ability to blend in with the surroundings, hide from enemies, and move undetected in natural environments.",
        "combat_bonuses": "None directly, though it allows the user to avoid combat or gain surprise."
      },
      {
        "name": "Hunting",
        "description": "The skill to find food in the wild, ensuring the Kai Lord never starves. Also provides basic agility.",
        "combat_bonuses": "None."
      },
      {
        "name": "Sixth Sense",
        "description": "An intuitive ability to sense imminent danger, hidden enemies, or true intent.",
        "combat_bonuses": "None directly, but helps avoid ambushes."
      },
      {
        "name": "Tracking",
        "description": "The ability to follow footprints, tracks, and read the signs of the wild to locate creatures or people.",
        "combat_bonuses": "None."
      },
      {
        "name": "Healing",
        "description": "The ability to heal physical wounds through Kai training.",
        "combat_bonuses": "Restores 1 Endurance Point (EP) for every section of the book passed without entering combat."
      },
      {
        "name": "Weaponskill",
        "description": "Mastery of a specific weapon type (e.g., Sword, Axe, Bow).",
        "combat_bonuses": "+2 Combat Skill (CS) when armed with the mastered weapon."
      },
      {
        "name": "Mindblast",
        "description": "The ability to attack enemies using the power of the mind.",
        "combat_bonuses": "+2 CS in combat against enemies who are not immune to psychic attacks."
      },
      {
        "name": "Animal Kinship",
        "description": "The ability to communicate with and understand animals, and sometimes calm or command them.",
        "combat_bonuses": "None."
      },
      {
        "name": "Mind Over Matter",
        "description": "Basic telekinesis; the ability to move small objects with the mind.",
        "combat_bonuses": "None."
      },
      {
        "name": "Mindshield",
        "description": "Mental defense against psychic attacks.",
        "combat_bonuses": "Prevents the loss of CS or EP when subjected to enemy psychic attacks."
      }
    ],
    "magnakai_disciplines": [
      {
        "name": "Weaponmastery",
        "description": "Advanced mastery of multiple weapon types.",
        "combat_bonuses": "Initially +3 CS with mastered weapons. Increases by +1 CS for every Magnakai level achieved."
      },
      {
        "name": "Animal Control",
        "description": "Enhanced Animal Kinship. The ability to command and control hostile animals and creatures.",
        "combat_bonuses": "None directly."
      },
      {
        "name": "Curing",
        "description": "Enhanced Healing. The ability to cure diseases, neutralize poisons, and heal wounds faster.",
        "combat_bonuses": "Restores 1 EP per section without combat. Can be used to heal others or neutralize status ailments."
      },
      {
        "name": "Invisibility",
        "description": "Enhanced Camouflage. The ability to mask body heat, muffle sound, and blend perfectly into terrain, as well as minor physical alterations.",
        "combat_bonuses": "None directly."
      },
      {
        "name": "Huntmastery",
        "description": "Enhanced Hunting. Grants the ability to see in the dark, incredible agility, and amplified senses.",
        "combat_bonuses": "None directly."
      },
      {
        "name": "Pathsmanship",
        "description": "Enhanced Tracking. The ability to read foreign languages, detect magic, and find the safest path in unnatural environments.",
        "combat_bonuses": "None directly."
      },
      {
        "name": "Psi-surge",
        "description": "Enhanced Mindblast. A powerful mental attack that drains the user's own energy to devastate foes.",
        "combat_bonuses": "+4 CS in combat at the cost of losing 2 EP per round. Alternatively, can use a weaker attack for +2 CS with no EP cost."
      },
      {
        "name": "Psi-screen",
        "description": "Enhanced Mindshield. Complete protection from advanced magical and psychic assaults.",
        "combat_bonuses": "Absorbs psychic damage and prevents negative CS modifiers from enemy mental attacks."
      },
      {
        "name": "Nexus",
        "description": "Enhanced Mind Over Matter. Move heavy objects with the mind and withstand extremes of heat and cold.",
        "combat_bonuses": "None directly."
      },
      {
        "name": "Divination",
        "description": "Enhanced Sixth Sense. The ability to leave the physical body (spirit journey), detect illusions, and communicate telepathically.",
        "combat_bonuses": "None directly."
      }
    ],
    "magnakai_lore_circles": [
      {
        "name": "Circle of Fire",
        "required_disciplines": ["Weaponmastery", "Huntmastery"],
        "bonuses": {
          "combat_skill": "+1 CS",
          "endurance_points": "+2 EP"
        }
      },
      {
        "name": "Circle of Light",
        "required_disciplines": ["Animal Control", "Curing"],
        "bonuses": {
          "combat_skill": "0 CS",
          "endurance_points": "+3 EP"
        }
      },
      {
        "name": "Circle of Solaris",
        "required_disciplines": ["Invisibility", "Huntmastery", "Pathsmanship"],
        "bonuses": {
          "combat_skill": "+1 CS",
          "endurance_points": "+3 EP"
        }
      },
      {
        "name": "Circle of Spirit",
        "required_disciplines": ["Psi-surge", "Psi-screen", "Nexus", "Divination"],
        "bonuses": {
          "combat_skill": "+3 CS",
          "endurance_points": "+3 EP"
        }
      }
    ],
    "grand_master_disciplines": [
      {
        "name": "Grand Weaponmastery",
        "description": "Supreme mastery over all hand-to-hand and missile weapons.",
        "combat_bonuses": "Initially +5 CS with any weapon. Increases as Grand Master ranks are achieved."
      },
      {
        "name": "Animal Mastery",
        "description": "Supreme command over the animal kingdom. Can summon and control beasts to fight for or assist the user.",
        "combat_bonuses": "None directly, but summoned animals can assist in combat."
      },
      {
        "name": "Deliverance",
        "description": "Supreme healing. The ability to instantly heal grievous wounds, including broken bones, and cure virulent plagues.",
        "combat_bonuses": "Can restore up to 20 EP during combat (once per adventure)."
      },
      {
        "name": "Assimilance",
        "description": "Supreme stealth. The ability to shift physical appearance, create illusions, and become entirely undetectable.",
        "combat_bonuses": "None directly."
      },
      {
        "name": "Grand Huntmastery",
        "description": "Supreme sensory awareness. Telescopic/microscopic vision, thermal imaging, and peak physical acrobatics.",
        "combat_bonuses": "None directly."
      },
      {
        "name": "Grand Pathsmanship",
        "description": "Supreme navigation and detection. Can instantly dispel illusions, detect traps, and instinctively know the lore of an area.",
        "combat_bonuses": "None directly."
      },
      {
        "name": "Kai-surge",
        "description": "Supreme psychic attack. A devastating mental assault capable of destroying lesser minds instantly.",
        "combat_bonuses": "+8 CS in combat at the cost of losing 1 EP per round. Alternatively, can use a weaker attack for +4 CS with no EP cost."
      },
      {
        "name": "Kai-screen",
        "description": "Supreme mental defense. Absolute protection against psychic intrusion, mind control, and telepathic tracking.",
        "combat_bonuses": "Completely negates any CS or EP loss from magical or psychic attacks."
      },
      {
        "name": "Grand Nexus",
        "description": "Supreme telekinesis and elemental resistance. Can pass through solid objects, survive in vacuums or lava, and move massive boulders.",
        "combat_bonuses": "None directly."
      },
      {
        "name": "Telegnosis",
        "description": "Supreme divination. Unrestricted astral projection, remote viewing across vast distances, and deep telepathic probing.",
        "combat_bonuses": "None directly."
      }
    ],
    "new_order_grand_master_disciplines": [
      {
        "name": "Magi-magic",
        "description": "Mastery of Old Kingdom battle-magic. Allows the user to cast powerful spells of the Elder Magi, such as Splinter, Flameshaft, and Strength.",
        "combat_bonuses": "Varies by spell; can provide temporary combat enhancements or allow for magical ranged attacks that increase Combat Skill."
      },
      {
        "name": "Kai-alchemy",
        "description": "Mastery of the Brotherhood of the Crystal Star magic. Grants access to spells such as Lightning Hand, Slow Fall, and Breathe Water.",
        "combat_bonuses": "Provides magical attacks (like Lightning Hand) that can be used to deal direct damage or gain a CS advantage."
      },
      {
        "name": "Astrology",
        "description": "The ability to read the cosmos, predict future events, sense celestial anomalies, and expertly use navigational and cosmological instruments.",
        "combat_bonuses": "None directly, though foresight can help anticipate enemy tactics or avoid fatal ambushes."
      },
      {
        "name": "Herbmastery",
        "description": "Advanced botanical knowledge. Allows the Grand Master to identify rare flora, brew powerful potions, and purify contaminated water or food.",
        "combat_bonuses": "None directly, but enables the creation of potions that restore Endurance Points or grant temporary buffs."
      },
      {
        "name": "Elementalism",
        "description": "The power to manipulate the elements of Earth, Air, Fire, and Water. The user can condense water from air, accelerate rust on metals, and control environmental elements.",
        "combat_bonuses": "Can be used strategically to destroy enemy equipment (like rusting ferrous weapons) or manipulate battlefield terrain."
      },
      {
        "name": "Bardsmanship",
        "description": "Mastery of music, voice, and performance. The ability to use songs and instruments to charm, calm, or distract creatures, alongside an encyclopedic knowledge of oral history.",
        "combat_bonuses": "Can pacify hostile creatures, distract enemies, or disrupt enemy concentration, occasionally bypassing combat entirely."
      }
    ]
  }
}
```

## Save_and_Load_Rules
- Saves must include all data
- A save name must include the following:
  - Book name, taken from `Gamebook_Metadata`
  - Page number
  - User-entered session name
- On loading, a modal will prompt the user which book and page to go to in order to resume

## Application Functionality
- Allow the user to add and remove items, gold crowns and special items from inventory, adhering to the `Inventory_Rules` section above
- Allow the user to add and remove free-form notes. Notes should include a book reference selected as a dropdown. Book selection is from the list of books in `Gamebook_Metadata` only
- Allow the user to add and remove meals
- Allow the user to increase and decrease maximum combat skill and maximum endurance
- Allow the user to increase and decrease current combat skill and current endurance. Neither can go above the maximum or below 0
- Allow the user to simulate combat as per the rules in `Combat_Algorithm`
- Allow the user to add and remove skills in the `Kai_Skills` list to their `current_skills_list`.
  - Where the user has added all skills required for a `magnakai_lore_circle`, the resulting CS and EP bonuses should be added to the current CS and EP maximums to show an effective CS and EP maximum. These are the values that should be used for combat
- Allow the user to save and load their game according to the rules in `Save_and_Load_Rules`