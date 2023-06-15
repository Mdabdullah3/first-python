# Python List (list change able )
fruitsList = ["apple", "banana", "cherry", "apple", "cherry"]
fruitsList[0] = "jack fruit"
print(fruitsList)
studentList = ["abir", 43, True]
print(studentList)
print(studentList[1])
# Add item list
studentList.insert(2, "computer")
print(studentList)
studentList.append("Diploma Engineering")
print(studentList)
# Remove From List
studentList.remove("computer")
print(studentList)
studentList.pop(2)
print(studentList)
studentList.pop()
print(studentList)
del studentList[1]
print(studentList)
studentList.clear()
print(studentList, "No List")
# Python - Loop Lists
# For Loop
heroine = ["Keya Payel", "toya", "Tisha"]
for item in heroine:
    print(item)
# Using Range
for i in range(len(heroine)):
    print(i)
# While Loop
luckyNumber = [23, 42, 44, 12]
i = 0
while i < len(luckyNumber):
    print(luckyNumber[i])
    i = i + 1
# Looping Using List Comprehension
[print(x) for x in luckyNumber]
# list comprehension
numbers = [212, 232, 3232]
for i in numbers:
    print(i * 2)
double = [i * 5 for i in numbers]
print(double)
# python Sort List
sortNumber = [3, 4, 34, 4, 5, 2]
sortNumber.sort()
print(sortNumber)
sortString = ["a", "f", "g", "s", "t", "d"]
sortString.sort()
print(sortString)
# Reverse List
sortString.sort(reverse=True)
print(sortString)
# Copy a List
listItem = ["cat", "dog", "cow", "lion", "tiger"]
copyList = listItem.copy()
print(copyList)
# Join Two List
joinList1 = [1, 2, 3]
joinList2 = [4, 5, 6, "Tamim"]
# joinTotal = joinList1 + joinList2
joinList1.extend(joinList2)
print(joinList1)
