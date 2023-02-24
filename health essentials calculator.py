# python weight converter

weight=float(input("Enter your weight in kilograms:\n "))
height=float(input("Enter your height in meters: \n"))
gender=input("enter your gender, enter male or female \n")
age=float(input("enter your age: \n"))

if gender.lower()=="male":
    bmr=13.397*weight + 4.799*height - 5.677*age + 88.362
else:
    bmr=9.247*weight + 3.098*height - 4.330*age+ 447.593

bmi = weight/(height**2)
ponderal_index= weight/(height**3)
avg_calories=weight*27

print(f"your Body mass index is{bmi}")
print(f"Your ponderal index is {ponderal_index}")
print(f"The average calories that you should consume is {avg_calories}")
