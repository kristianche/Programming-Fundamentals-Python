import math
number_of_people = int(input())
number_of_people_per_on_course = int(input())
courses = math.ceil(number_of_people / number_of_people_per_on_course)
print(courses)


