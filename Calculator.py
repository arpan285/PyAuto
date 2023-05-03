class Cal:
    def __init__(self, a,b):
        print("This is parametrized constructor")
        self.x = a
        self.y = b
    def addition(self):
        print("ANS=",self.x+self.y)

    def subs(self):
        print("ANS=",self.x-self.y)

num = int(input("Enter first number: "))
num1 = int(input("Enter another number: "))

obj = Cal(num,num1)
obj.addition()
obj.subs()