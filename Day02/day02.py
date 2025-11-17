print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))      
tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / num_people   
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")


"""
Sample Output:

Welcome to the tip calculator!
What was the total bill? $150
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 5
Each person should pay: $33.60
"""
