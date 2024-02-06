#OOP -> Object Oriented Programming
    #Example 1 of an Object(Hamid is an object)
        #Attributes=> Name, Age, Sex, Phone...
        #Methods=> Playing, talking, Sleeping, Eating, Reading, Coding...
    #Example 2 of an Object(Cat is an object)
        #Attributes=> Color, Age, Sex...
        #Methods=> Playing, sounding, Sleeping, Eating...

# How to create a class
#1-Define the Class
class Animal:
    #Here you can define variables(characteristics) and methods(actions)
    #1.1-Define a variable
    sound = "No sound yet!"
    #1.2-Define a method
    def make_sound(self):
        #self is just for this animal.
        print(self.sound)
#2-Create an instance(example of the Class)
my_animal = Animal() #Here we created a specific animal using our class
#3-Display the features = variables = characteristics of the clas
print("Features of the Animal Class:")
print("*"*100)
print(Animal.__dict__) #Shows the features
print("*"*100)
print("\nFeatures of my_animal Instance:")
print("*"*100)
print(my_animal.__dict__) #Shows the features of our animal
print("*"*100)
#4-Make the Animal instance do an action
print("\nMaking the animal instance do an action:")
print("*"*100)
my_animal.make_sound() #The animal perform the action