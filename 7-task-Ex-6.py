# Task 7:  Program to find repeated elements in a tuple

data = (1,6,8,0,1,1,2,2,4)
data_in_list = []
repeated_num = []
many_time_repeated = []

for num in data:
    if num not in data_in_list:
        data_in_list.append(num)
    elif num in repeated_num:
        many_time_repeated.append(num)
    else:
        repeated_num.append(num)  
    
if repeated_num:
    print(f'Repeated  nums are {repeated_num}')
else:
    print('No repeated nums')
