a=float(input("Enter the first angle: "))
b=float(input("Enter the second angle: "))
c=float(input("Enter the third angle: "))
sum_of_angles =a+b+c
if a>0 and b>0 and c>0 and sum_of_angles == 180:
    print("yes, it forms a triangle")
else:
    print("no, it does not form a triangle")