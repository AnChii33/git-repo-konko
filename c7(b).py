# Display output for series: x+x/1!+(x^2)/2!+(x^3)/3!+...+(x^n)/n!
# x, n => USER INPUT
import math as m
x=int(input("Enter value of x: "))
n=int(input("Enter value of n: "))
sn=x
for i in range(1, n+1):
    sn+=(x**i)/m.factorial(i)
print(sn)