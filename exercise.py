# Problem 1 : Print the second in fruit list
fruitList = ["apple", "banana", "jackfruit", "mango", "cherry", "dates"]
print(fruitList[1])
# Problem 2 : Change the value from "apple" to "kiwi", in the fruits list.
fruitList[0] = "Kiwi"
print(fruitList)
# Problem 3 : Use the append method to add "orange" to the fruits list.
fruitList.append("Orange")
print(fruitList)
# Problem 4 : Use the insert method to add "lemon" as the second item in the fruits list.
fruitList.insert(1, "Lemon")
print(fruitList)
# Problem 5 : Use the remove method to remove "banana" from the fruits list.
fruitList.remove("banana")
print(fruitList)
# Problem 6 :  Use negative indexing to print the last item in the list.
print(fruitList[-1])
# Problem 7 :  Use a range of indexes to print the third, fourth, and fifth item in the list.
item = fruitList[2:5]
for i in item:
    print(item)
# Problem 8 :  Use the correct syntax to print the number of items in the list.
print(len(fruitList))
