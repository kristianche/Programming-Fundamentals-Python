class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    line = input()
    if line == "End":
        break
    else:
        party.people.append(line)
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")