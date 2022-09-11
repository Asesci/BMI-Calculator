length = float(input("Your length (in cm): "))
weight = float(input("Your weight (in kg): "))

length = length / 100
bmi = weight / length ** 2

print(f"Your BMI is {bmi}")
