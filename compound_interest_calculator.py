while True:
    amount = float(input("Enter the amount: "))
    if amount < 0:
        print("Amount can't be less than 0")
    else:
        break

while True:
    rate = float(input("Enter the rate: "))
    if rate < 0:
        print("Rate can't be less than 0")
    else:
        break

while True:
    time = int(input("Enter the time: "))
    if time < 0:
        print("Time can't be less than 0")
    else:
        break

total = amount*pow((1+rate/100), time)
print(f"Balance after {time} years: {total:.2f}$")
