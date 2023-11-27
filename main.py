import alpha
import beta
import charlie
from deltaFolder.delta import printing_myFileName

try:
    charlie.get_user_age()
    printing_myFileName()
except ValueError:
    print("That's not a valid value for your age!")