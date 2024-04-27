# Task 6: Write a program to remove duplicates from a list

my_list = [10, 20, 30, 20, 40, 10, 50, 30]
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)      

