#01 create a dictionary 

students = {
    "name": "Ali",
    "age": 20,
    "course": "BS Computer Science",
    "city": "Karachi"
}

print(students["name"])
print(students["age"])
print(students["course"])
print(students["city"])






# 02 Add an update dic values 
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2018
}

car["color"] = "white"
car["year"] = 2022

print(car)








# 03 Find frequency of elements in list using dictionary
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)










# 04 Count frquency of words 
sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)








# 06 calaculate the total and average marks 
marks = {
    "math": 80,
    "english": 70,
    "physics": 90
}

total = 0

for subject in marks:
    total += marks[subject]

average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)









# 07 Find highest scoring student
students = {
    "ali": 85,
    "sara": 92,
    "ahmed": 78,
    "zara": 95
}

highest_student = ""
highest_marks = 0

for name in students:
    if students[name] > highest_marks:
        highest_marks = students[name]
        highest_student = name

print("Highest scoring student:", highest_student)
print("Marks:", highest_marks)
