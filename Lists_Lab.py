#LISTS LAB

#A function to sum all items in a list
def sum_items(list:list):
    sum = 0
    for element in list:
        sum+=element
    print("The sum is {}".format(sum))

sum_items([1,2,3,4,5,6])

#A function to get the largest number from a list
def largest_number(list:list):
    list.sort()
    print("The largest number is {}".format(list[-1]))

largest_number([5,0,9,2,3,7,6])

#odd numbers list in the range 1200-2000 with steps of 125 using list comprehension
odd_numbers_list = [number for number in range(1200,2000,125) if number%2 == 1]
print(odd_numbers_list)

#using list slicing to get the list from the first element to the 5th element
sliced_list = odd_numbers_list[:5]
print(sliced_list)