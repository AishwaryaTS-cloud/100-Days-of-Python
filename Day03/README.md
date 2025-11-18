# 🚀 Day 03 – 100 Days of Coding

Today I continued learning Python from the **Udemy – Complete Python Bootcamp by Angela Yu** and moved into one of the most important parts of programming: **Conditional Statements**.

I also built a fun mini-adventure game using everything I learned today.

---

## 📚 What I Learned Today

- Conditional Statements
- Modulo Operator
- Nested `if`
- Logical Operators

All topics are from the **Udemy Python Course – Complete Python Bootcamp by Angela Yu**.

---

## 🧩 Project — Treasure Island (Choose-Your-Own-Adventure Game)

For today’s project, I built a story-based decision game where the user has to choose different paths to find the treasure.

---

## 📌 Code

```python
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |              |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|______________| ;`-.o`"=._; ." ` '`."'` . "-._ /_______________|___
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_§/__/__/__/__/__/__/__/__/__/__/______/______/______/__/
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake. There's an island in the middle.\n"
                    "Type 'wait' to wait for a boat.\n"
                    "Type 'swim' to swim across: ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive safely at the island. There is a house with 3 doors: red, yellow, blue.\n"
                        "Which one do you choose? ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("That door doesn't exist. Game Over.")
    else:
        print("You were attacked by a trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

```

---

## 🌱 Day 03 Summary

Today's lesson was all about decision-making in Python.

I learned how computers react differently based on conditions and combined those skills to build an interactive adventure game. A super fun and solid day of progress.

---