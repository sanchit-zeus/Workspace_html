#booleans
True
False
0
1

#tuples
t=(1,2,3);
print(t[0]);

t=("a",True,123);
print(t);
#t[0]="new";#they are immutable just like strings, assignment will not be done

#sets
#only takes unique elements, once an element is in the set it will not enter again
x=set();
x.add(1);
x.add(2);
x.add(3);
x.add(4);
x.add(5);
print(x);

x=set();
x.add(2);
x.add(2);
x.add(4);
x.add(4);
x.add(5);
print(x);

converted=set([1,1,1,1,2,2,2,2,3,3,3]);
print(converted);
