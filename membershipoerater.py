# in Returns true if a variable is in sequence of another variable, else false.
# not in Returns true if a variable is not in sequence of another variable, else false.

# program to check number if exist in list
a=10  
b=21  
list=[10,20,30,40,50];  
if (a in list):  
    print ("a is in given list") 
else:  
    print ("a is not in given list") 
if(b not in list):  
    print ("b is not given in list")  
else:  
    print ("b is given in list")
    



# identity operator
# is Returns true if identity of two operands are same, else false
# is not Returns true if identity of two operands are not same, else false.

a=20
b=20
if(a is b):
    print("a,b have same identity")
else:
        print("a,b is difference")
b=10
if(a is not b):
    print("a,b have different identity")
else:
        print("a,b have same identity")