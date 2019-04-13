#inheritance
class Animal():
    def __init__(self):
        print("Animal Created")
    def whoAmI(self):
        print("Animal")
    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        print("dog Created")
    def bark(self):
        print("woof")
    def whoAmI(self):
        print("Dog")
    def eat(self):
        print("Dog Eating")
mydog=Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()

#special methods
class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):#used to give out string
        return "Title: {},Author: {}, Pages: {}".format(self.title,self.author,self.pages)
    def __len__(self):#a length is assigned
        return self.pages
    def __del__(self):#used to delete object
        print("a book is destroyed")

b=Book("python","sanchit",200)
# print(b)#to print the variable through objectwe have to use special function
# print(len (b))#object doesnt have any special length use special method len to give it one
del b
