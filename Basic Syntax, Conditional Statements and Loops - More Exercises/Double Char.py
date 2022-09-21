string = input()
while string != "End":
    if string != "SoftUni":
      print()
      for character_index in string:
        text = ""
        text += 2 * character_index
        print(text, end="")
    string = input()
