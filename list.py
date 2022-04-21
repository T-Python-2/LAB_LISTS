#Q1
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([10,20,30]))

#Q2
list1 = [10, 20, 4, 45, 99]
print(max(list1))

#Q3
oddList =[n for n in range(1200,2000,125)if n%2 != 0 ]
print(oddList)  

#Q4
prevList = ["A","B","C","D","E","F","G"]
newList = list()
newList = newList + prevList[:5]

print(prevList)
print(newList)