text = "  Hello Python Programming  "

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Strip:", text.strip())

# Split
words = text.split()
print("Split:", words)

# Join
print("Join:", "-".join(words))

# Replace
print("Replace:", text.replace("Python", "Java"))

# Find
print("Find:", text.find("Python"))