print("\nWelcome to the tip calculator\n")
bill = float(input("What was the total bill? £"))
party_size = float(input("How many people to slpit the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? "))

tip = (bill/tip_percentage)
total_bill = bill+tip
bill_per_person = total_bill/party_size
#round(bill_per_person, 2)
final_bill = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: £{final_bill}")