#ask user for their name
name = input("what's your name? ")

#remove whitespace from string
name = name.strip()

#capitalize users name
name = name.title()

#say hello to user
print(f"hello, {name}")
