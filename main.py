
### Q1: Write a Python program to sum all the items in a list.

my_list = [1,2,3,4,5]
total = sum(my_list)

print("Sum of all elements in the list: ", total)
    
### Q2: Write a Python program to get the largest number from a list.

max_num = max(my_list)
print("The largest number from a lis: ", max_num)

### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.

odd_list = [n for n in range(1200,2000,125) if n % 2 !=0]
print(odd_list)

### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

newList = list()
newList = newList + odd_list[:5]

print(newList)
