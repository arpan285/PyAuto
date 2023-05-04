class Cal:
    def __init__(self, a,b):
        print("This is parametrized constructor")
        self.x = a
        self.y = b
    def addition(self):
        print("Addition ANS=",self.x+self.y)

    def subs(self):
        print("Substraction ANS=",self.x-self.y)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

obj = Cal(num1,num2)
obj.addition()
obj.subs()