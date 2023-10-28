for i in range(5):
    print(i)


r = list(range(5,10))
print(r)

k = list(range(0,10,3))
print(k)

p = list(range(-10,-100,-30))
print(p)

#To iterate over the indices of a sequence, we can combine range() and len() as follows:
d = ['Mary','had','a','little','lamb']
for i in range(len(d)):
    print(i,d[i])


s = (sum(range(4)))
print(s)
