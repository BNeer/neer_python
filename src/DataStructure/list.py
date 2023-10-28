list1 = [1,2,4,5]
print(list1[1])

#Append
list1.append(8)
print(list1)

#Extend
Fruits1 = ["Mango", "Orange", "Apple"]
Fruits2 = ["Watermelon"]
Fruits1.extend(Fruits2)
print(Fruits1)

#insert
numbers = [10, 20, 30, 40, 50]
print(numbers.insert(2,99))
print(numbers)

#remove
fruits = ["apple", "banana", "cherry", "apple", "date"]
# Remove the first occurrence of "apple" from the list
fruits.remove("banana")
print(fruits)  # This will print: ["banana", "cherry", "apple", "date"]


########

##Remove 
fruits = ["apple", "banana", "cherry", "apple", "date"]
# Remove the first occurrence of "apple" from the list
fruits.remove("apple")
print(fruits)  # This will print: ["banana", "cherry", "apple", "date"]


#Pop
fruits = ["apple", "banana", "cherry"]
# Remove and return the last element from the list
last_fruit = fruits.pop()
print(last_fruit)  # This will print: "cherry"
print(fruits)  # This will print: ["apple", "banana"]

colors = ["red", "green", "blue", "yellow"]
new_colors = colors.pop(1)
print(new_colors)
print(colors)


###Clear

fruits = ["apple", "banana", "cherry", "date"]
fruits.clear()


##list.index(x[, start[, end]])
fruits = ["apple", "banana", "cherry", "date", "banana"]
# Find the index of the first occurrence of "banana"
index = fruits.index("banana")
print(index)  # This will print: 1

# Find the index of the first occurrence of "banana" starting from index 2
index = fruits.index("banana", 2)
print(index)  # This will print: 4

##list.count(x)
#Return the number of times x appears in the list.
fruits = ["apple", "banana", "cherry", "date", "banana"]
# Count the number of times "banana" appears in the list
count = fruits.count("banana")
print(count)  # This will print: 2






print(len(list1))


list2 = [6,7,2,9,1]
# Add 2 lists
list3 = [list1, list2]
print(list3[0][1])

#print(list4=[list1,list2])



#print(list2[2:])
#print(list2[-3:])



