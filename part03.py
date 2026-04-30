# 01 print alternate element of list
user_list = input("Enter list elements separated by space: ").split()

for i in range(0, len(user_list), 2):
    print(user_list[i])







# 02 Reverse without using reverse function
user_list = input("Enter list elements separated by space: ").split()

reversed_list = user_list[::-1]

print(reversed_list)








# 03 Find largest num without max function
user_list = input("Enter numbers separated by space: ").split()

numbers = []

for i in user_list:
    numbers.append(int(i))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)








# 04 Rotate of elements 
user_list = input("Enter list elements separated by space: ").split()

rotated_list = [user_list[-1]] + user_list[:-1]

print(rotated_list)









# 05 Delete n characters from start of string
text = input("Enter a string: ")
n = int(input("Enter number of characters to delete from start: "))

result = text[n:]

print(result)









# 06 Convert date format
date = input("Enter date in mm/dd/yyyy format: ")

month_list = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

parts = date.split("/")

month = int(parts[0])
day = parts[1]
year = parts[2]

print(month_list[month] + "/" + day + "/" + year)










# 07 Function to modify string
def modify_string(text):
    words = text.split()
    new_text = []

    for word in words:
        new_text.append(word.capitalize())

    return " ".join(new_text)

sentence = input("Enter a sentence: ")

result = modify_string(sentence)

print(result)







#  08sum of each row in matrix 
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix = []

for i in range(m):
    row = input("Enter row elements separated by space: ").split()
    matrix.append([int(x) for x in row])

for i in range(m):
    row_sum = 0
    for j in range(n):
        row_sum += matrix[i][j]
    print("Sum of row", i + 1, "is", row_sum)


















# 09 sum of two matrices
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

matrix1 = []
matrix2 = []
result = []

print("Enter elements of first matrix:")
for i in range(m):
    row = input().split()
    matrix1.append([int(x) for x in row])

print("Enter elements of second matrix:")
for i in range(m):
    row = input().split()
    matrix2.append([int(x) for x in row])

for i in range(m):
    row = []
    for j in range(n):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Resultant Matrix:")
for row in result:
    print(row)










# 10 Multiply two matrices
m = int(input("Enter number of rows of first matrix: "))
n = int(input("Enter number of columns of first matrix: "))
p = int(input("Enter number of columns of second matrix: "))

matrix1 = []
matrix2 = []
result = []

print("Enter elements of first matrix:")
for i in range(m):
    row = input().split()
    matrix1.append([int(x) for x in row])

print("Enter elements of second matrix:")
for i in range(n):
    row = input().split()
    matrix2.append([int(x) for x in row])

for i in range(m):
    row = []
    for j in range(p):
        sum = 0
        for k in range(n):
            sum += matrix1[i][k] * matrix2[k][j]
        row.append(sum)
    result.append(row)

print("Resultant Matrix:")
for row in result:
    print(row)
