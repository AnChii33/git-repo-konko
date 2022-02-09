# Display output for series: 1+x+x^2+x^3+...+x^n
# x, n => USER INPUT

x=int(input("Enter value of x: "))
n=int(input("Enter value of n: "))
sn=1
for i in range(1, n+1):
    sn+=x**i
print(sn)