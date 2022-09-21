counter = int(input())
for i in range(1, counter + 1):
    code = int(input())
    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif code < 88 and code != 86:
        print("GREAT!")
    elif code > 88:
        print("Bye.")