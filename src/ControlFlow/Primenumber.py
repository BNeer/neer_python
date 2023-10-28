
#for (i=0, i<=9,i++):
#c = 0
#   for (j=1,j<=i,j++):
#       if i%j == 0
#          c++
#   if C < = 2
#      print(i is a prime number)
#   else 
#      print(i is not a prime number)


for i in range(1,10):
    c = 0
    
    for j in range(1, i+1):
        if i % j == 0:
            c += 1 

    if c <= 2:
        print(f'{i} is a prime number' ) 
    else :
        print(f'{i} is not a prime number') 
            
    

    
   

