class Dog():
    #class object attribute same for all instances
    species="mammal"



                      #breed is the arguement
    def __init__(self,breed,name):#self tell that method belongs to itself (class dog)
        self.breed=breed#initialisation special method
        self.name=name

mydog=Dog(breed="Lab",name="sammy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)

#################################
class Circle():
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
    def area(self): #self keyword tells that the method is of the class
        return self.radius*self.radius*Circle.pi
    def set_radius(self,new_r):
        self.radius=new_r

myc=Circle(radius=3)
myc.set_radius(999)
print(myc.radius)#specially called variables to print them
print(myc.area)
print(myc.area())
