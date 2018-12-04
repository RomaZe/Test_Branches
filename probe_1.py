class Snow:

    def __init__(self, color, hight):
        self.color = color
        self.hight = hight

    def __str__(self):
        return "Snow color: {color}, how much: {height}".format(color=self.color, height=self.hight)


def total(a, b):
    return a + b


day1 = Snow('white', 10)
print(day1)


