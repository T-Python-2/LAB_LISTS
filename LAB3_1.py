##Write a Python program to sum all the items in a list.
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,3,4,5,6,7,8,9]))


##Write a Python program to get the largest number from a list.


def max_num_in_list(list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1,2,3,4,5,6,7,8,9,100]))


##Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using list comprehension.


A_list =[x for x in range(1200, 2000, 125) if x%2 != 0]

print(A_list)

##use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
'''
'''
org_list=list()
new_list=[1,2,3,4,5,6,7,8,9,10]
org_list=new_list[3:]
print(org_list)