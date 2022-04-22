
### Q1: Write a Python program to sum all the items in a list.
num_list = [2 , 4 , 6 , 8 , 10 , 12 , 14 , 16]
print("summation is : " , sum(num_list))
# Another solution (with for loop)
sum = 0
for i in num_list:
    sum += i 
print("Sum :",sum)



### Q2: Write a Python program to get the largest number from a list.
print("The largest number is :" , max(num_list))


### Q3: Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.

odds_list = [num for num in range(1200 , 2000, 125 ) if num % 2 != 0]
print(odds_list)


### Q4: use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

sliced_list = num_list[:5]
print(sliced_list)