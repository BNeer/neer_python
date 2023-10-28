knights = {'gallahad': 'the pure', 'robin': 'the brave'}
h = knights.items()
print(h)
for k,v in knights.items():
    print(k,v)


#When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)


## Zip() Function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    print('what is your {0} ? It is {1}.'.format(q,a))



#Loop over a sequence in reverse 
for i in reversed(range(1,10,2)):
    print(i)


#sorted() function ->It returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

#set() -> eliminates duplicate elements
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
    print(i)


#
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for v in raw_data:
    if not math.isnan(v):
        filtered_data.append(v)
print(filtered_data)

    
