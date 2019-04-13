x=25

def my_func():
    x=50
    return x

print(x)
print(my_func)

my_func()
print(x)

###########################################
#local
lambda x:x**2

#eclosing function locals

name="This is a global name!"

def greet():
    # name="sammy"

    def hello():
        print("hello "+name)
    hello()
greet()
###########################################
x=50

def func(x):
    print("x is :",x)
    x=1000
    print("local x changed to:",x)

func(x)
print(x)
#######################
def func():
    # global x
    x=1000
    return x

print("before function call, x is: ",x)
x=func()
print("after function call, x is: ",x)
