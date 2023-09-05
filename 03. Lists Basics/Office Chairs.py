numbers_of_rooms = int(input())
needed_chairs = 0
total_free_chairs = 0
flag = True
for room in range(1, numbers_of_rooms + 1):
    chairs_and_visitors = input().split(" ")
    chairs = chairs_and_visitors[0]
    visitors = int(chairs_and_visitors[1])
    if len(chairs) >= visitors:
        free_chairs = len(chairs) - visitors
        total_free_chairs += free_chairs
    else:
        needed_chairs = visitors - len(chairs)
        flag = False
        print(f"{needed_chairs} more chairs needed in room {room}")
if flag:
    print(f"Game On, {total_free_chairs} free chairs left")



