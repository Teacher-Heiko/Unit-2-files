
s = "KMIDS"

for c in s:
    if c == 'I' or c == "U":
        print("There is an I or U in", s)
    if c in 'IU':
        print("There is an I or U in", s)