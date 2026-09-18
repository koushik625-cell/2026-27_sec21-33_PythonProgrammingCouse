#python logical Operators exercise
a=5
result = a > 2 and a < 10 #logical and Operators
print("result of",a,">2 and",a,"<10 is",result)

result = a < 2 or a > 10 #logical or Operators
print("result of",a,"<2 or",a,">10 is",result)

result = not(a > 2 and a < 10) #logical not Operators
print("result of not(",a,">2 and",a,"<10) is",result)

result = a < 2 and a > 10 #logical and Operators
print("result of",a,">2 and",a,"<10 is",result)

result = a > 2 or a < 10 #logical or Operators
print("result of",a,"<2 or",a,">10 is",result)

result = not(a < 2 and a > 10) #logical not Operators
print("result of not(",a,">2 and",a,"<10) is",result)