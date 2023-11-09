def solution(inputArray):
    outputList = []
    for i in range(len(inputArray)-1):
        k = inputArray[i] * inputArray[i+1]  
        outputList.append(k)  # Append the result to the output list
        
    answer = max(outputList)
    return answer
 


inputArray = [0,1,0,100]
ans = solution(inputArray)
print(ans)

















#########################################################################




# inputArray = [3, 6, -2, -5, 7, 3]

# result = []
# def solution(inputArray):
#     for i in inputArray:
#         k = i * i
#         #list.append(i[0]*i[0+1])
#         result.append(k)

# solution(inputArray)


# print(result)

###########################################################################




    