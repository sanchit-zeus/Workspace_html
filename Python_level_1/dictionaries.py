
my_stuff={"key1":"value","key2":"value2"}
print(my_stuff["key2"]);

my_stuff={"key1":123,"key2":"value2","key3":{"123":[1,2,3]}}
print(my_stuff["key3"]);

#to grab a specific element
my_stuff={"key1":123,"key2":"value2","key3":{"123":[1,2,"grab me"]}}
print(my_stuff["key3"]["123"][2].upper());

#redefining dictionaries
my_stuff={"lunch":"pizza","bfast":"eggs"};
my_stuff["lunch"]="Burger";
print(my_stuff["lunch"])
my_stuff["dinner"]="pasta";
print(my_stuff);
