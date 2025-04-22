print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))


tip_percent = tip / 100
tip_amount = tip_percent * bill
total_with_tip = bill + tip_amount

bill_per_person = total_with_tip / people

# Format to 2 decimal places (e.g., $30.00 instead of $30.0)
final_amount = round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")
