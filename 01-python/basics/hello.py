#Ask user for their name.
name = input("Whats your name? ")
#Remove whitespace from the name.
name = name.strip()
#Capitalize user's name.
name = name.capitalize()
#Capitalize the first letter of each word in the name.
name = name.title()
#Remove whitespace and capitalize the name again to ensure proper formatting.
name = name.strip().title()
#split user's name into first and last name.
first, last = name.split(" ")
#Say hello to the user.
print(f"Hello, {first}")
#I can also do this:name = input("Whats your name? ").strip().title()
