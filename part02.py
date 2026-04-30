# 01 Bonus based on salary and years of service
# Taking input from user
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

# Bonus calculation
if years_of_service > 5:
    bonus = salary * 0.05
else:
    bonus = 0

# Output
print("Net Bonus Amount:", bonus)








# 02 Check voting eligibility based on age

# Taking input from user
age = int(input("Enter your age: "))

# Checking eligibility
if age > 17:
    print("Eligible for voting")
else:
    print("Not eligible for voting")






# 03 Check even or odd number 
number = int(input("Enter a number: "))

# Checking even or odd
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")






# 04 Check divisibility by 7
number = int(input("Enter a number: "))

if number % 7 == 0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")






# 05 Check multiple of 5
number = int(input("Enter a number: "))

if number % 5 == 0:
    print("Hello")
else:
    print("Bye")







# 06 Display last Digit of a number 
number = int(input("Enter a number: "))

last_digit = number % 10

print("Last digit is:", last_digit)






# 07 Check square of rectangle 
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

if length == breadth:
    print("Square")
else:
    print("Rectangle")







# 08 Find greatest of two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Greatest number is:", num1)
else:
    print("Greatest number is:", num2)







# 09 Shop Discount Calculation
quantity = int(input("Enter quantity: "))

unit_price = 100

total_cost = quantity * unit_price

if total_cost > 1000:
    discount = total_cost * 0.10
    total_cost = total_cost - discount

print("Total cost:", total_cost)








# 10 Grade Calculation based on marks
marks = int(input("Enter marks: "))

if marks < 25:
    print("Grade: F")
elif marks < 45:
    print("Grade: E")
elif marks < 50:
    print("Grade: D")
elif marks < 60:
    print("Grade: C")
elif marks < 80:
    print("Grade: B")
else:
    print("Grade: A")






# 11 Attendance Percentage Calculation
classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100

print("Attendance Percentage:", attendance_percentage)

if attendance_percentage >= 75:
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam")









# 12 Employee calculation
age = int(input("Enter age: "))
gender = input("Enter gender (M or F): ")
marital_status = input("Enter marital status (Y or N): ")

if gender == "F" or gender == "f":
    print("She will work only in urban areas")

elif gender == "M" or gender == "m":
    if age >= 20 and age < 40:
        print("He may work anywhere")
    elif age >= 40 and age <= 60:
        print("He will work only in urban areas")
    else:
        print("ERROR")
else:
    print("ERROR")










# 13 Leap Year Check
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
