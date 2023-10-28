basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

'orange' in basket


a = set('abracadabra')
b = set('alacazam')

print(a)

print(a-b)          # # letters in a but not in b


print(a | b )                             # letters in a or b or both

print(a&b)                              # letters in both a and b

print(a^b)                   # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)