cols = 6
letters = [chr(ord('A') + i) for i in range(26)]

top =    "╔" + "╦".join(["═══"] * cols) + "╗"
middle = "╠" + "╬".join(["═══"] * cols) + "╣"
bottom = "╚" + "╩".join(["═══"] * cols) + "╝"

print(top)

for i in range(0, len(letters), cols):
    row = letters[i:i+cols]
    
    row += [' '] * (cols - len(row))
    print("║ " + " ║ ".join(row) + " ║")
    if i + cols < len(letters):
        print(middle)

print(bottom)
