from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division
from Calculator.square import square
from Calculator.sqrt import sqrt


class Calculator:
    result=0

    def __init__(self):
        pass

    def add(self,a,b):
        self.result = addition(a,b)
        return self.result

    def subtract(self,a,b):
        self.result=subtraction(a,b)
        return self.result

    def multiply(self,a,b):
        self.result=multiplication(a,b)
        return self.result

    def div(self,a,b):
        self.result=division(b,a)
        return self.result

    def square(self,a):
        self.result=square(a)
        return self.result

    def sqrt(self,a):
        self.result = sqrt(a)
        return self.result