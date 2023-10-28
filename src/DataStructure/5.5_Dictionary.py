tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])

#k = del tel['sape']
#print(k)


print(list(tel))   #['jack', 'sape', 'guido']

print(sorted(tel))

l = {x:x**2 for x in (2,4,6)}
print(l)