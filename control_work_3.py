class SquareOrRectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def calculation(self):
        file = open("square_or_rectangle.txt", "a")
        if self.side_a == self.side_b:
            square_area = self.side_a ** 2
            data = ("This is square, it's area equals " + str(square_area) + "\n")
            file.write(str(data))
        elif self.side_a != self.side_b:
            rectangle_area = self.side_a * self.side_b
            data = ("This is rectangle, it's area equals " + str(rectangle_area) + "\n")
            file.write(str(data))
        file.close()


while True:
    x = input("Enter side 'a' length: ")
    y = input("Enter side 'b' length: ")
    if not(x.isdigit() and y.isdigit()):
        print("Value must be integer!")
    else:
        x = int(x)
        y = int(y)
        shape = SquareOrRectangle(x, y)
        shape.calculation()
    stop = input("Do you want to add some more data?(y/n): ")
    if stop == "y":
        continue
    elif stop == "n":
        break
    else:
        print("Invalid value")
