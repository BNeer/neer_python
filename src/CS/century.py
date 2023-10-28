def century(year):
    # Calculate the century
    if year % 100 == 0:
        result = year // 100
    else:
        result = year // 100 + 1
    return result

year = 1205  # Replace this with the year you want to calculate the century for
result = century(year)  # Call the function and store the result in 'result'
print(f"For year {year}, the century is {result}")


centurt(1207)




#1 ≤ year ≤ 2005
# 1 to 100 
# 101 to 200 
# 1601 to 1700 -> 17
# 1901 - 2000 -> 20 


