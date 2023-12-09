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

