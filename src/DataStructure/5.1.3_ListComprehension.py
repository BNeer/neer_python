squares = []
for x in range(10):
    squares.append(x**2)
print(squares)



sqaures = list(map(lambda x: x**2,range(10)))
print(squares)


squares = [x**2 for x in range(10)]
print(squares)


vec = [-4,-2,0,2,4]
b = [x*2 for x in vec]
print(b)

# filter the list to exclude negative numbers
c = [x for x in vec if x > 0]
print(c)


from math import pi
[str(round(pi, i)) for i in range(1, 6)]
#['3.1', '3.14', '3.142', '3.1416', '3.14159']