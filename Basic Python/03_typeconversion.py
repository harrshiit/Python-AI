#Type converison in python is done in two ways 

#1. Type conversion --> Done  by python  itself 
#example 
a=10 
b= 5 
print(a/5) # Automatically convert into decimal result  2.0
print(type(a/5)) # answer will be float

# another example
ans = 5+10.0 
print (type(ans))  # float 


#2. Type Casting ---> implicit conversion done by developer himself
 #exmaple
ans1 =int(5+10.0)
print(ans1 , type(ans1)) # result  15  & int type 

ans2=bool(-10)
print(  ans2 , type(ans2))#number other than 0 is always true in boolean type prints--> True bool

