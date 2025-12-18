n = 0

while n != -1:
    n = int(input("Quekke table ? "))

    for i in range(10):
        print(f"{i} * {n} = {n*i}")
