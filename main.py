import alpha
import beta
import charlie
from deltaFolder.delta import printing_myFileName
import echoFolder.echo as echo

try:
    charlie.get_user_age()
    printing_myFileName() #delta
    print(__name__)
except ValueError:
    print("That's not a valid value for your age!")

