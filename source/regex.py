import re

email = input("What is your email? ").strip()

print(email)
# getting user email
# r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.+$" <-- email regex
# r"^[a-zA-Z0-9_.]+@(\w+\.)*\w+\.$"
# r means raw string, ignoring escape characters
# ez email regex
if re.search(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.\w+$", email, re.IGNORECASE):
    # making sure the email entered matches the regex
    print("Valid")
else:
    print("Nipples")
