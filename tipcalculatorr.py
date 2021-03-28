print("WELCOME TO TIP CALCULATOR!!")
total = float(input("What was the toal bill? \n"))

percent=int(input("What percent of tip would you like to give?10,12 or 15? \n"))

tip_percentage= int((total*percent)/100)

people = int(input("How many people to split the bill? \n"))

final_pay= (total + tip_percentage)/people

print(f"Each person should pay: {final_pay}")