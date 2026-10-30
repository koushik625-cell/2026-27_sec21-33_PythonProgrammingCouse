text = input("Enter a string: ")

for ch in text:
    if text.index(ch) == text.find(ch):
        print(ch, "=", text.count(ch))