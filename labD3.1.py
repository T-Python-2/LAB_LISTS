#q1 Write a Python program to sum all the items in a list.
from pickle import APPEND


my_list = [1, 7, 4]

sum_list = 0

for i in range(0,len(my_list)):
     sum_list += my_list[i]

print(sum_list)

#q2 Write a Python program to get the largest number from a list.
list2 = [1, 7, 4, 11, 6]

print(max(list2))

#q3 Create an odd numbers list from the elements of a range from 
#1200 to 2000 with steps of 125, using list comprehension.


list3 = list()
for i in range(1200, 2000, 125):
    if i %2 != 0:
        list3.append(i)
    else:
        continue

print(list3)

even_nums = [x for x in range(1200, 2000, 125) if x %2 != 0]
print(even_nums)
    
#q4 use list slicing to get a new list from the previous list starting
#  from the start to the 5th element in the list.
list4 = [1, 7, 4, 11, 6, 4, 9, 2]
new_list4 = list4[:5]
print(new_list4)
