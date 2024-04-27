# Task 6:Write a program to get a smallest number from a list

marks = [77,81,93,97,99]
smallest_num = marks[0]
for num in marks:
    if num < smallest_num:
        smallest_num = num
print(f'Lowest mark is {smallest_num}')