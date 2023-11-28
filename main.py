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

dictionary_of_people = {0:Parent("Mary", 63), 1:Child("Megan", 35), 2:Child("Amanda", 25)}
for each_person in dictionary_of_people:
    display(dictionary_of_people[each_person])

print("---------------------")
print("Between " + dictionary_of_people[1].name + " and " + dictionary_of_people[2].name + ", " +compare_ages_of(dictionary_of_people[1], dictionary_list_of_people[2])+ " is the older")
print("Between " + dictionary_of_people[0].name + " and " + dictionary_of_people[2].name + ", " +compare_ages_of(dictionary_of_people[0], dictionary_list_of_people[2])+ " is the older")