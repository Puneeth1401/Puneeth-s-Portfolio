unit=int(input("Enter the number of units consumed:  "))
if unit <= 200:
    amount= (0.8*unit)+100
elif (unit>200) and (unit<= 300):
    amount=(200*0.8)+(unit-200)*0.9+100
else:
    amount= (200*0.8)+(100*0.9)+(unit-300)+100

if amount>400:
    amount=amount*0.15+amount

print(f"The total amount to be paid is {amount}")
