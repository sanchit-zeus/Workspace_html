#strings


#basics
'hello'
"hello"
mystring3="i'm a dog";
mystring2="BABA";
mystring1="me"; #strings are immutable so te previous value would be forgotten
x=mystring1.upper();#converts to uppercase
print(x);
y=mystring2.lower();#converts to lowercase
print(y);
z=mystring1.capitalize();#capitalize only the first letter
print(z);
w=mystring1.split();
print(w);
v=mystring3.split();#split is used to break the string
print(v);           #by default the split breaks at the space in stringand make a list
u=mystring3.split("m");#will split the string where m is present
print(u);

#indexing
mystring="abcdefg";
print(mystring);
print(mystring[0]);
print(mystring[1]);
print(mystring[-1]);#used for displsying last index

#slicing
print(mystring[4:]);#from 4 till end
print(mystring[:3]);#from starting till 3 not including 3
print(mystring[2:5]);
print(mystring[::]);#grabs everything
print(mystring[::1]);#step size of one grabs everything
print(mystring[::2]);#step size of two grabs every second element

#print formatting

#inserts another string into another
a="Insert another string here: {}".format("Insert Me")
print(a);

b="Insert Item one: {c} Item Two:{d}".format(c="Dog",d="Cat");
print(b)
