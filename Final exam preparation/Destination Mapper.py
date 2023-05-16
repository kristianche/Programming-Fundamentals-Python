import re
string = input()
pattern = r"(\=|\/)([A-Z])([A-Za-z]{2,})\1"
result = re.finditer(pattern, string)
points = 0
all_destinations = []
for destination in result:
    current_destination = re.split("\/|=", destination.group())[1]
    points += len(current_destination)
    all_destinations.append(current_destination)
print(f"Destinations: {', '.join(all_destinations)}")
print(f"Travel Points: {points}")