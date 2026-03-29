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