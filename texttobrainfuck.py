from __future__ import print_function
text = str(raw_input("text: "))
text = [ord(c) for c in text]
Values = []
for i in text:
    Value = int(round(i, -1))
    if Value > i:
        UpDown = "down"
        HowMuch = Value-i
    else:
        UpDown = "up"
        HowMuch = abs(Value - i)

    Values.append([Value, UpDown, HowMuch])
Compact = str(raw_input("Compact: "))
if Compact == "no":
    print("++++++++++")
    print("[")
    for i in Values:
        print("    > " + "+"*(i[0]/10))
    print("<"*len(Values) + "-")
    print("]")

    for i in Values:
        if i[1] == "up":
            print("> " + "+"*i[2] + ".")
        else:
            print("> " + "-"*i[2] + ".")
else:
    print("++++++++++", end="")
    print("[", end="")
    for i in Values:
        print(">" + "+"*(i[0]/10), end="")
    print("<"*len(Values) + "-", end="")
    print("]", end="")

    for i in Values:
        if i[1] == "up":
            print(">" + "+"*i[2] + ".", end="")
        else:
            print(">" + "-"*i[2] + ".", end="")
