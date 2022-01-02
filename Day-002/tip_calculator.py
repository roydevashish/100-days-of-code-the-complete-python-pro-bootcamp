#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
amount = float(input("What was the total bill? $"))
person = float(input("How many people to split the bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip_amount = (amount/100)*tip
total_amount = amount + tip_amount
each_person = total_amount / person

print(f"Each person should pay: ${round(each_person, 2)}")