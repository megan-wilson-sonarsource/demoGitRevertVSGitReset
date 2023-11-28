import alpha
import beta
import charlie
from deltaFolder.delta import printing_myFileName
import echoFolder.echo as echo
import girl

try:
    charlie.get_user_age()
    printing_myFileName() #delta
    print(__name__) # Script Mode
except ValueError:
    print("That's not a valid value for your age!")

