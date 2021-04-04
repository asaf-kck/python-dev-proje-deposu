a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

Delta = b ** 2 - 4 * a * c

x1 = (-b + Delta ** 0.5) / 2 * a
x2 = (-b - Delta ** 0.5) / 2 * a

print("Kök1: {}\nKök2: {}".format(x1,x2))