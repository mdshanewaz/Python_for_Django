class A:
    def __init__(self, nam):
        self.name = nam

    def hello(self):
        print("Hello form A")

class B:
    def __init__(self, job):
        self.possition = job

    def hello(self):
        print("Hello form B")

class C(A, B):
    pass

class D(B, A):
    pass

obj1 = C("Shawon")
obj1.hello()
print(dir(obj1))

obj2 = D("Shawon")
obj2.hello()
print(dir(obj2))
