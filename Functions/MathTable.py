
def math_table(x, y):
    print("Enter the number to find its multiplication table:", x)
    print("Enter the range of the table:", y)

    result = []
    for i in range(1, y+1):
        result.append(x*i)
        print(x, 'X', y, '=', result)
       
    return result


x = int(input("Enter the number to find its multiplication table: "))
y = int(input("Enter the range of the table: "))

results = math_table(x, y)


print(results)
