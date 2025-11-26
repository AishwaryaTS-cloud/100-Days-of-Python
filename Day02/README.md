## 🚀 Day 02 – 100 Days of Coding

Today I worked on number manipulation concepts from the **Udemy – Complete Python Bootcamp by Angela Yu** and built a practical mini-project: **Tip Calculator**.

---

## 📚 What I Learned Today

- Python primitive data types
- Type checking with `type()`
- Type conversion using `int()`, `float()`, `str()`
- Mathematical operations in Python
- Number manipulation using `int()`, `round()`, and **f-strings**

---

## 🧩 Project — Tip Calculator

This beginner-friendly project calculates how much each person should pay when splitting a bill with a chosen tip percentage.

The program asks for:

- Total bill amount
- Tip percentage
- Number of people splitting the bill

Then it returns the amount each person should pay.

---

## 📌 Code

```python
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / num_people

final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")

```

### 🎯 Sample Output

```
Welcome to the tip calculator!
What was the total bill? $150
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 5
Each person should pay: $33.60

```

---

## 🌱 Day 02 Summary

Good progress today — practiced converting data types, formatting numbers, and applying math operations in a real project. The tip calculator helped me understand how these concepts work together in practical programs.

---