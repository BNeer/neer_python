pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key=lambda pair:pair[1])
print(pairs)


#sort() is a method that can be applied directly to a list, whereas sorted() is a built-in function that can be used with any iterable (e.g., lists, tuples, strings).
#sort() is an in-place sorting method, which means it sorts the list it's called on and modifies the original list. It doesn't return a new sorted list but rather sorts the elements in the existing list.
#sorted() is a built-in function that takes an iterable, sorts its elements, and returns a new sorted list, leaving the original iterable unchanged.
#sort() is generally more efficient when sorting a list if you don't need to keep the original order because it operates in-place and doesn't create a new list. This can be important for large datasets where memory usage is a concern.
#sorted() is useful when you want to sort an iterable and keep the original data intact or when dealing with data structures other than lists

numbers = [5,2,8,1,3]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)