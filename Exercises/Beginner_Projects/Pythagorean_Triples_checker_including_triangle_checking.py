print("Please input side a, b, and c, where c is the longest.")

print("Please input side a.")
a=float(input())

print("Please input side b.")
b=float(input())

print("Please input side c (aka longest side).")
c=float(input())

print("Please input side a, b, and c, where c is the longest.")

if (c**2) == (a**2 + b**2):
    print("This is a Pythagorean triangle.")
elif a<b+c and b<a+c and c<a+c:
    print("This is a triangle.")
else:
    print("This is NOT even a triangle.")
