#Example 1
animals = ["cat", "dog", "rabbit", "hamster"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars / len(animals)))    

#Example 2
Winners = ["Alice", "Bob", "Charlie"]
for index, winner in enumerate(Winners):
    print("Winner {}: {}".format(index + 1, winner))

#Example 3
def fill_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(fill_emails([("alice@example.com", "Alice"), ("bob@example.com", "Bob"), ("charlie@example.com", "Charlie")]))
