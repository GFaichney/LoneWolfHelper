# Ignore everything in this file - these are notes only

Phase 4: Starting Equipment

1. Roll for Starting Gold
- If the chosen book's subseries is `Kai`, pick a random number between 1 and 10. Add 10 to it
- If the chosen book's subseries is `Magnakai`, pick a random number between 1 and 10. Add 10 to it
- If the chosen book's subseries is `Grand Master`, pick a random number between 1 and 10. Add 20 to it

2. Equipment
- If the chosen book is a Kai book, gain 2 random items from the list below:
```JSON
{
      "random_equipment_table": [
        { "roll": 1, "item": "Sword", "type": "Weapon" },
        { "roll": 2, "item": "Helmet", "type": "Special Item", "effect": "+2 ENDURANCE" },
        { "roll": 3, "item": "Two Meals", "type": "Backpack Item" },
        { "roll": 4, "item": "Chainmail Waistcoat", "type": "Special Item", "effect": "+4 ENDURANCE" },
        { "roll": 5, "item": "Mace", "type": "Weapon" },
        { "roll": 6, "item": "Healing Potion", "type": "Backpack Item", "effect": "Restores 4 ENDURANCE" },
        { "roll": 7, "item": "Quarterstaff", "type": "Weapon" },
        { "roll": 8, "item": "Spear", "type": "Weapon" },
        { "roll": 9, "item": "12 Gold Crowns", "type": "Currency" },
        { "roll": 0, "item": "Broadsword", "type": "Weapon" }
      ]
    }
```

- If the chosen book is a Magnakai book, allow the user the choice of 5 items from the list below:
```JSON
"starting_equipment_options": [
        { "item": "Sword", "type": "Weapon" },
        { "item": "Bow", "type": "Weapon" },
        { "item": "Quiver", "type": "Special Item", "notes": "Contains 6 arrows" },
        { "item": "Rope", "type": "Backpack Item" },
        { "item": "Potion of Laumspur", "type": "Backpack Item", "effect": "Restores 4 ENDURANCE" },
        { "item": "Lantern", "type": "Backpack Item" },
        { "item": "Mace", "type": "Weapon" },
        { "item": "3 Meals", "type": "Backpack Item" }
      ]
```

- If the chosen book is a Grand Master book, allow the user the choice of 5 items from the list below:
```JSON
"starting_equipment_options": [
        { "item": "Sword", "type": "Weapon" },
        { "item": "Bow", "type": "Weapon" },
        { "item": "Quiver", "type": "Special Item", "notes": "Contains 6 arrows" },
        { "item": "Dagger", "type": "Weapon" },
        { "item": "Rope", "type": "Backpack Item" },
        { "item": "Potion of Laumspur", "type": "Backpack Item", "effect": "Restores 4 ENDURANCE" },
        { "item": "Lantern", "type": "Backpack Item" },
        { "item": "Mace", "type": "Weapon" },
        { "item": "3 Meals", "type": "Backpack Item" }
      ]
```


## Extra Combat Logic:
In the combat tab, when calculating the player's combat skill, if a weapon is used that matches that chosen for the player's weaponskill discipline (if they have it) then +2 CS should be added.

Sommerswerd checkbox should only be available if the player has the Sommerswerd in their special items

**If** In Combat:
  - **If** Sommerswerd is checked:
    - **If** the Player has Grand Weaponmastery, add 5 CS
    - **else if** the player has Magnakai discipline of Weaponmastery with `Sword` as one of the weapons, add 3 CS
    - **else** if the player has the Kai discipline of Weaponskill with `Sword` as the weapon, add 2 CS
  - **else**
  - **If** the player has selected a weapon from the `Weapon in hand` dropdown
      - **If** the Player has Grand Weaponmastery, add 5 CS
      - **else if** the player has Magnakai discipline of Weaponmastery with the selected weapon as one of the weapons, add 3 CS
      - **else** if the player has the Kai discipline of Weaponskill with the selected weapon, add 2 CS

If Sommerswerd is checked, the `Weapon in hand` dropdown should be changed to say 'Sommerswerd'


# Book switching logic
- The UI should allow the player to change books to another book (next_book), with the following rules:
  - next_book must be after the current book in the Gamebook_Metadata as given in `Instructions.md`
  - The current book should be added to a list of completed books
- When changing book, apply the following logic:
  - **If** next_book.suberies == 'Kai':
    - Add 1D10 + 10 gold to the current gold total, adhering to the maximum of 50
    - Allow the user to choose an additional Kai discipline as per the rules at character creation
  - **If** next_book.suberies == 'Magnakai':
    - **If** the current book subseries == 'Kai':
      - Allow choice of 3 Magnakai skills as per Character_Creation_Logic
      - All weapons and backpack items can be kept
      - Only the following special items can be carried over to the new book (other should be removed and the player informed):
        - (Kai) Shield
        - Crystal Star Pendant
        - (Battered) Padded Leather Waistcoat
        - Helmet
        - Chainmail Waistcoat
        - Sommerswerd
        - Firesphere
        - Silver Helm
        - Dagger of Vashna
        - Herb Pad
        - Canteen of Water
        - Jeweled Mace
    - Add 1D10 + 10 gold to the current gold total, adhering to the maximum of 50
    - **If** the current book subseries == 'Magnakai':
      - Allow the user to choose an additional Magnakai discipline as per the rules at character creation
        - **If** the player already has Weaponmastery
       - **then** allow them to add an additional weapon to the list
       - **elif** the player chooses Weaponmastery then allow them to choose 3 weapons PLUS 1 additional weapon for each completed Magnakai book 
  - **If** next_book.suberies == 'Grand Master':
    - Change the maximum backpack size to 10 items
    - **If** the current book subseries == 'Magnakai' or 'Kai':
      - Allow the selection of 4 Grand Master disciplines as per Character_Creation_Logic
      - All weapons and backpack items can be kept
      - Only the following special items can be carried over to the new book (other should be removed and the player informed):
        - Crystal Star Pendant
        - Sommerswerd
        - Silver Helm
        - Dagger of Vashna
        - Jeweled Mace
        - Silver Bow of Duadon
        - Helshezag
        - Kagonite Chainmail
    - Add 1D10 + 10 gold to the current gold total, adhering to the maximum of 50
    - **If** the current book subseries == 'Grand Master':
      - Allow the player to choose an additional Grandmaster discipline as per the character creation rules


## Kai Monastery
- Any number of backpack items, weapons and special items can be transferred to the Kai Monastery inventory. This can only be done when switching books
- Any number of backpack items, weapons and special items can be transferred from the Kai Monastery inventory. This can only be done when switching books. Backpack, special item and weapon limits must still be observed

## Random number generation
- Provide the player a button to generate a random number between 0 and 9. This should be present at the top of all tabs

## Midblast in Combat
- **If** the player has the Kai discipline of Mindblast:
  - Provide a checkbox to use Mindblast.
  **If** In combat and Mindblast is checked:
  - If checked, the Player's effective combat skill is increased
  - Each round of combat that is rolled, the player loses 2 EP
  - If the user has < 2 EP then the round cannot be rolled until Mindblast is unchecked

## Additional Save Game Logic
- **If** the player clicks save game and the game was previously loaded from disk:
  - Pre-populate the `Session Name` field with the previous session name
  - Overwrite the previous save once `Save` button is clicked