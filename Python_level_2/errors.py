# try:
#    you do your operation here....
#    ....
# except ExceptionI:
#     if there is an exceptionI, then execute this blockself.
# except ExceptionII:
#     if there is an exceptionII, then execute this blockself.
#     ....
# else:
#     if there is no exception then execute this block.

try:
    f=open("simple.txt","w")
    f.write("test write to simple text!")
except IOError:
    print("error: could not find or read data!")
else:
    print("success!")
    f.close()
######################################################

    try:
        f=open("simple.txt","r")
        f.write("test write to simple text!")
    except:
        print("error: could not find or read data!")
    else:
        print("success!")
        f.close()
print("hello world!")

#############################################3

try:
    f=open("simple.txt","r")
    f.write("test write to simple text!")
except:
    print("error: could not find or read data!")
finally:
    print("i always work no matter what!")
