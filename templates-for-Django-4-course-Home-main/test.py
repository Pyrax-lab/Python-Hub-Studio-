class Yo:

    __slots__ = "a", "b"

    def __init__(self, a, b):

        self.a = a
        self.b = b

    def get(self):
        print(self.a, self.b)


a = Yo(1, 3)
a.get()
