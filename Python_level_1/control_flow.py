if 1<2:
    if 2<3:
        print('True!')

if 1<2:
    print("First block")
    if 20<3:
        print('Second block')

if 1==1:
    if 1>2:
        print("hello!")
    elif 3==3:
        print("elif ran")
    else:
        print("Last")


#for loop list
seq=[1,2,3,4,5,6];

for item in seq:
    #code here
    print(item)

for item in seq:
    #code here
    print("Hello")

#for loop dictionary
    d={"sam":1,"frank":2,"dan":3}
for item in d:#it will print keys
    print(item)

for k in d:
    print(k)
    print(d[k])

# for tuples
mypairs=[(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item)

for (tup1,tup2) in mypairs:#seperated the (tuples unpacking)
    print(tup2)#firts item
    print(tup1)#second item

#while loop
i=1;
while i<5:
    print("i is: {}".format(i))
    i=i+1


#range fuctions
#can quickly generates function for you based on starting and ending point


#list comprehension
x=[1,2,3,4]

# out=[]
# for num in x:
#     out.append(num**2)
#
# print(out)

out=[num**2 for num in x]#this is list comprehension
print(out)
