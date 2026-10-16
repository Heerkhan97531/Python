# write a program that print the sum of first n natural numbers
n =int(input("enter a number:" ))
sum =0

while(n>=1):
    sum = sum+n
    n=n-1

print("sum =", sum)
print("n = ", n)