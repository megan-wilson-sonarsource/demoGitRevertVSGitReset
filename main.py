from alpha import Alpha
import bravo
import charlie
from deltaFolder.delta import printing_myFileName
import echoFolder.echo as echo
import girl
from parent import Parent
from child import Child

def compare_ages_of(a, b):
    if a.age > b.age:
        return(a.name)
    else:
        return(b.name)
my_alpha = Alpha()
print(my_alpha.greet())
try:
    charlie.get_user_age()
    printing_myFileName() #delta
    print(__name__) # Script Mode
except ValueError:
    print("That's not a valid value for your age!")

person1 = Parent("Mary", 63)
person2 = Child("Megan", 35)
person3 = Child("Amanda", 25)
print("---------------------")
print("Name: " + person1.name)
print("Age: " + str(person1.age))
print("Relationship: " + person1.relationship)
print(person1.saying)
print("DISPLAY:")
person1.display()
print("---------------------")
print("Name: " + person2.name)
print("Age: " + str(person2.age))
print("Relationship: " + person2.relationship)
print(person2.saying)
print("DISPLAY:")
person2.display()
print("---------------------")
print("Name: " + person3.name)
print("Age: " + str(person3.age))
print("Relationship: " + person3.relationship)
print(person3.saying)
print("DISPLAY:")
person3.display()
print("---------------------")
print("Between " + person2.name + " and " + person3.name + ", " +compare_ages_of(person2, person3)+ " is the older")
print("Between " + person1.name + " and " + person3.name + ", " +compare_ages_of(person1, person3)+ " is the older")