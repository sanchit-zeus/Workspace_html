#lists
#list are mutable

mylist=[1,2,3];
mylist=["asbhcjajfmk",1,2,3,4,True,"dwfegdf",[1,2,3]]
mylist=["a","b","c","d","e"];
print(len(mylist));
print(mylist[0]);
print(mylist[:3]);

mylist[0]="New Item";#lists are mutable
print(mylist);
mylist.append("New Item");#dont affect any item just append a item at the end of the list
print(mylist);
mylist.append(["x","y","z"]);#list becomes a part of it
print(mylist);
mylist.extend(["f","g","h","i"]);#this extends the lists
print(mylist);

#removal
mylist2=["a","b","c","d","e"];
item=mylist2.pop();
print(mylist2);
print(item);
item=mylist2.pop(0);
print(mylist2);
print(item);

mylist3=["a","b","c","d","e"];
mylist3.reverse();#this occurs in place. which menas that we dont have to save it in any item
print(mylist3);#dont try to sort multiple datatype in list, not a good practice

mylist4=[194,825,36,47,85,66];
mylist4.sort();
print(mylist4);

mylist5=[1,2,["x","y","z"]];
print(mylist5[2][0]);#nested list. to get x out of the other nested list.

#list comprehension
matrix=[[1,2,3],[4,5,6],[7,8,9]];
first_col=[row[0] for row in matrix]

print(first_col);
