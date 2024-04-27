# Task 6: Write a program to get a largest number from a list

marks = [77,81,93,97,99]
largest_num = marks[0]
for num in marks:
    if num > largest_num:
        largest_num = num
print(f'Highest mark is {largest_num}')
