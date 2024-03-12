''' 
This application calculates the portion of bill each person pays when  bill is distributed equally among a group.
'''
# Create a greeting for your program.
print("Welcome to the Tip Calculator!")

# Ask the user for the total bill amount
bill = int(input("What was the total bill? (Enter amount in dollars but without the $ sign. e.g. write 150.20 for $150.20)\n"))
# Ask the user for the tip percentage they like to give
tip = int(input("How much tip would you like to give? (Enter a percentage amount without the '%' sign. E.g. write 10 for 10%)\n"))
# Ask the uder for the number of people to split the bill
num_people = int(input("How many people to split the bill?\n"))

# Calculate total bill per person
bill_per_person = (bill*(1+tip/100))/num_people
print(f"Each person should pay: $ {bill_per_person:.2f}")
