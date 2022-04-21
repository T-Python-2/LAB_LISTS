#Q1
myList = [5,10,10,20,5,50]
sum = 0
for n in myList:
    sum += n
print(sum)

#Q2
print(max(myList))

#Q3
oddList = list()
for n in range(1200,2000,125):
    oddList.append(n)
print(oddList)  

#Q4
prevList = ["A","B", "C","D","E","F","G"]
newList = list()
newList = newList + prevList[:5]

print(prevList)
print(newList)