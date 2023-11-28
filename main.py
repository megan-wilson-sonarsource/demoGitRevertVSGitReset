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

def display(person):
    print("---------------------")
    print("Name: " + person.name)
    print("Age: " + str(person.age))
    print("Relationship: " + person.relationship)
    print(person.saying)
    print("DISPLAY:")
    person.display()

my_alpha = Alpha()
print(my_alpha.greet())
try:
    age = charlie.get_user_age()
    new_age = int(charlie.add_1_to(age))
    print("Next year you will be: "+ str(new_age))
    printing_myFileName() #delta
    print(__name__) # Script Mode
except ValueError:
    print("That's not a valid value for your age!")

person1 = Parent("Mary", 63)
person2 = Child("Megan", 35)
person3 = Child("Amanda", 25)
display(person1)
display(person2)
display(person3)
print("---------------------")
print("Between " + person2.name + " and " + person3.name + ", " +compare_ages_of(person2, person3)+ " is the older")
print("Between " + person1.name + " and " + person3.name + ", " +compare_ages_of(person1, person3)+ " is the older")