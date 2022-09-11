height = float(input("Your height (in cm): "))
weight = float(input("Your weight (in kg): "))

height = height / 100
bmi = weight / height ** 2

print(f"Your BMI is {bmi}")
