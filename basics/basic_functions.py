 # !def armstrong(num) :
#     a = num
#     cube = 0
    
#     while(num > 0):
#         cube = cube + (num%10)**3
#         num //= 10
    
#     if cube == a :
#         print(f"{a} is an armtsrong number")
    
#     else :
#         print(f"{a} is not an armtsrong number")

# armstrong(153)

# # !Arbitrary Arguments, *args
# def num(name,*data) :
#     print(f"{name}  \n {data}")

# num('shinchan',1,2,3,3,4,"4.5S",5)
    
# # !Arbitrary Keyword Arguments, **kwargs
# def num2(name,**data) :
#     print({name})
#     print(data.items())

# num2('shinchan', age=5, lname="Nohara")

# ! Lambda
# square_lambda = lambda x: x**2
# print(square_lambda(50))

# x = lambda a : a * 10
# print(x(10))

# y = lambda a , b, c : a + b + c 
# print(y(5,3,2))
# from functools import reduce

# nums = [1,2,3,4,8,8,9,0]

# # def is_even (a) :
# #     return a %2==0

# evens = list(filter(lambda n : n%2==0 , nums))
# double_even = list(map( lambda n : n * 2, evens))

# # sum = reduce()

# print(evens)
# print(double_even)

# class subject :
#     def __init__(self , pa1 , pa2 ,pa3 ,pa4 , final ):
#         self.pa1 = pa1
#         self.pa2 = pa2
#         self.pa3 = pa3
#         self.pa4 = pa4
#         self.final = final
    
#     def score(self):
#         finalscore = (self.pa1 + self.pa2 + self.pa3 + self.pa4 + self.final)
#         print(finalscore)
        
# maths = subject(0,9,8,10,45)
# maths.score()

# def div(a,b):
#     if a<b:
#         a,b = b,a 
#     print( a/b)
    
# div(1,4)

# class calc:
#     def __init__(self, a, b):
#       self.a = a
#       self.b = b
    
#     def add(self):
#         print (self.a + self.b)

#     def diff(self):
#         print (self.a - self.b)
        
#     def product(self):
#         print (self.a * self.b)
    
#     def divide(self):
#         print (self.a / self.b)
    
# new_calc = calc(50 , 20)
# new_calc.add()
# new_calc.diff()
# new_calc.product()
# new_calc.divide()

# a = int(input("a :"))
# b = int(input("b :"))
# c = int(input("c :"))

# x = max(a,b,c)
# print(x)

# from math import *

# res = int(pow(2, 3))
# res1 = sqrt(3)

# print(res1)
# print(res)
# print(pi)

# import json





