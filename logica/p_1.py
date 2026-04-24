for i in range(0, 101):
    result = str(i)

    if i % 2 == 0:
        result += " buzz"

    if i % 5 == 0:
        result += " bazz"

    print(result)