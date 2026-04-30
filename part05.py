#01 Working with lists 
numbers = [10, 20, 15, 30, 25, 40, 35, 50]

total = 0

for num in numbers:
    print(num)
    total += num

print("Sum:", total)

for num in numbers:
    if num % 2 == 0:
        print("Even:", num)











# 02 Dictionary Basics 
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python",
    "marks": [60, 70, 80]
}

total = 0

for key in student:
    print(key, student[key])

for mark in student["marks"]:
    total += mark

average = total / len(student["marks"])

print("Average:", average)

if average >= 50:
    print("Passed")
else:
    print("Failed")











# 03 List of Dictionaries 
employees = [
    {"name": "Ali", "department": "IT", "salary": 50000},
    {"name": "Sara", "department": "HR", "salary": 60000},
    {"name": "Ahmed", "department": "Finance", "salary": 55000}
]

total_salary = 0
highest_salary = 0
highest_employee = ""

for emp in employees:
    print(emp)
    total_salary += emp["salary"]
    if emp["salary"] > highest_salary:
        highest_salary = emp["salary"]
        highest_employee = emp["name"]

print("Highest Salary Employee:", highest_employee)
print("Total Salary:", total_salary)










# 04 While loop with user inuput 
numbers = []

while True:
    num = int(input("Enter number (-1 to stop): "))
    if num == -1:
        break
    numbers.append(num)

print(numbers)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)












# 05 Count frequency of words
sentence = input("Enter sentence: ")
words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word in frequency:
    print(word, frequency[word])









# 06 Table with Nested loops 
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()
