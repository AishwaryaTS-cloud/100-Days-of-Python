# 🚀 Day 04 – 100 Days of Coding

Today was all about randomness and lists — two things that make Python a lot more fun.

I followed the **Udemy – Complete Python Bootcamp by Angela Yu**, and built a classic game using everything I learned.

---

## 📚 What I Learned Today

- The `random` module
- `random.randint()`, `random.random()`, `random.choice()`
- Lists
- Indexing & slicing
- List functions like `append()`, `extend()`, `insert()`, `remove()`, `pop()`
- How Python modules work and how to import them

All topics are from the **Udemy Python Course – Complete Python Bootcamp by Angela Yu**.

---

## 🧩 Project — Rock Paper Scissors Game

To wrap up the lesson, I created the Rock-Paper-Scissors game where the player goes against the computer.

This was a perfect mix of randomness, lists, and conditional logic.

---

## 📌 Code

```python
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))

if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number. You lose.")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose.")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("You lose.")

```

---

## 🌱 Day 04 Summary

Today was all about making programs feel alive.

I learned how to generate randomness, how lists store and organize data, and how to manage them using built-in functions. All of that came together in my Rock-Paper-Scissors game.

A simple project, but it really tied together everything from the last few days.

---