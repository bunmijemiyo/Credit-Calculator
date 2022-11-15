income = int(input())
if income < 15528:
    percent = "0"
    calculated_tax = income * 0
    print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
elif income < 42708:
    percent = "15"
    tax = income * 0.15
    calculated_tax = round(tax)
    print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
elif income < 132407:
    percent = "25"
    tax = round(income * 0.25)
    calculated_tax = round(tax)
    print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
elif income > 132406:
    percent = "28"
    tax = round(income * 0.28)
    calculated_tax = round(tax)
    print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")