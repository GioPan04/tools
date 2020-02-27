text = input("Text: ")
upp = ""
for c,i in enumerate(text):
    if (c + 1) % 2 == 1:
        upp = upp + i.upper()
    else:
        upp = upp + i.lower()

print(upp)
