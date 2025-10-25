
print("Welcome to BMI Calculator!")

userWeight = input("Enter Your Weight: ")
userHeight = input("Enter Your Height: ")

#str to int convertion
intuserWeight = float(userWeight)
intuserHeight = float(userHeight)

# Calculate BMI
calculateBMI = intuserWeight/(intuserHeight**2)
print("Your BMI Value is:",round(calculateBMI,2))
