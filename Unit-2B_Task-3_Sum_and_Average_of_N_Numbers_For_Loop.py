
# Program to find the sum and average of N numbers using for loop

n = int(input("Enter the number of values: "))

total = 0

for i in range(1, n + 1):
    num = float(input("Enter number {}: ".format(i)))
    total = total + num

average = total / n

print("Sum of", n, "numbers =", total)
print("Average of", n, "numbers =", average)
