# Create a new list
myFirstList = ["Lama", "Hala", "Nouf"]
print(myFirstList)
# Add a new value to the end of the list
myFirstList.append("Aroub")
print(myFirstList)
# Add a new value to a specific position in the list
myFirstList.insert(2, "Ghala")
print(myFirstList)
# print a specific value in the list
print(myFirstList[-2])

# Add a list to another one (merge them togther)
anotherList = ["Nasser", "Aziz"]
myFirstList.extend(anotherList)
print(myFirstList)
# concatinate two lists in a new list
new_list = myFirstList + anotherList
print(new_list)

# Delete an item from the list
new_list.pop(8)
print(new_list)
del new_list[7]
print(new_list)


# looping through a list
for i in myFirstList:
    print(i)


# Slicing a list
print(myFirstList[1:5])
print(myFirstList[:4])
print(myFirstList[3:])
