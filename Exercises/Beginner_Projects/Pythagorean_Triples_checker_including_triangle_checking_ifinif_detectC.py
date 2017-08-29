print("Please input side a, b, and c.")

def side_sorter():
    global a
    global b
    global c
    sides = []
    for i in range(3):
        sides.append(int(input()))
    hypotenuse = max(sides)
    c = hypotenuse
    sides.remove(c)
    a = sides[0]
    sides.remove(a)
    b = sides[0]

def Pythagorean_triangle_checker():
    if a<b+c and b<a+c and c<a+c:
        if (c**2) == (a**2 + b**2):
            print("This is a Pythagorean triangle.")
            exit()
            print("This is a triangle.")
        else:
            print("This is NOT even a triangle.")

side_sorter()
Pythagorean_triangle_checker()
