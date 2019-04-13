def my_func(param1="default"):
    """
    THIS IS THE DOCSSTRING
    """
    print("my first python function!{}".format(param1))
my_func("zee")

########################################
def hello():
    print("hello")
hello()
########################################
def hello():
    return("hello")
result=hello()
print(result)
########################################
def addNum(num1,num2):
    return num1+num2

result=addNum(2,3)
print(result)
print(type(result)) #returns the type of class of the return type
#####################################################
def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return"sorry, i need an integer!"

result=addNum(2,3)
print(result)
print(type(result))
######################################################

#lambda expression
#has no name anonymous function
mylist=[1,2,3,4,5,6,7,8]
evens=filter(lambda num:num%2==0,mylist)
print(evens)

#filter function

def even_bool(num):
    return num%2==0

evens=filter(even_bool,mylist)
print(list(evens))
###################################################
#in operator
#test fo the presence of any item
print("x"in[1,2,3,"x"])
