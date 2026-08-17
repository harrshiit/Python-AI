#A lambda function is a small, anonymous (unnamed) function in Python. 
# It is used to create simple functions in a single line without using the def keyword.

#way1
def square(x):
    return x*x

numbers=[1,2,3,4]
result=list(map(square,numbers))
print(result)

# way2 using lambda expression 
numbers = [1, 3, 4]
result = list(map(lambda x: x ** 2, numbers))
print(result)
