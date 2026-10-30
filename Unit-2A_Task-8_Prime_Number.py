num = int(input("Enter a number (1 to 100): "))

if num <= 1:
    print("Not a Prime Number")
else:
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print("Prime Number")
    else:
        print("Not a Prime Number")