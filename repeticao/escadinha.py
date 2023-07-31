n = int(input())

for numero in range(1, n + 1):
    for i in range(1, numero + 1):
        if numero == i:
            print(i, end='')
        else:
            print(i, end=' ')
    print()
