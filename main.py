my_list = [ 1, 2, 3, 4, 5]

#Q1
sum = 0
for element in my_list:
    sum = sum + element

print (sum)


#Q2
print(max(my_list))

#Q3
odd_list = list()
for element in range(1200,2000,125):
    if element % 2 == 0:
        continue
    else:
        odd_list.append(element)

print(odd_list)


#Q5
scal_list = list()
new_list = [1,2,3,4,5,6,7,8]
scal_list = new_list[5:]
print(scal_list)