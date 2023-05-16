countries = input().split(", ")
capitals = input().split(", ")
data = zip(countries, capitals)
my_dict = {country: capital for (country, capital) in data}
for key, value in my_dict.items():
    print(f"{key} -> {value}")