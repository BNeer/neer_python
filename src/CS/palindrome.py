def solution(inputString):
    return inputString == inputString[::-1]


result = solution('a')
print(result)
result = solution('abc')
print(result)
