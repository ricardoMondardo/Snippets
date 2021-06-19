import re

# Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:





# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.

# If the username is valid then your program should return the string true, otherwise return the string false.
# Examples


pattern = r"[a-zA-Z][a-zA-Z0-9_]{3,6}[^_]$"
sequence = "a1_a1*"


if re.match(pattern, sequence):
    print("Match!")
else: print("Not a match!")