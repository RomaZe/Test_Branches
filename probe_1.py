class Snow:

    def __init__(self, color, hight):
        self.color = color
        self.hight = hight

    def __str__(self):
        return "Snow color: {color}, how much: {height}".format(color=self.color, height=self.hight)

class Child:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Child name is {}".format(self.name)


def total(a, b):
    return a + b

x = 5
y = 5
z = x + y

day1 = Snow('white', 10)
igor = Child("Igor")
print(day1)
print(igor)


