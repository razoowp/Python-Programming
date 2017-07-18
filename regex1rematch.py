# re.match function can be used to determine whether it matches at the beginning
#of a string.

import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No Match")
