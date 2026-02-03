# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem


n = int(input())

names_phones_dict = {}
for _ in range(n):
    line = input().split()
    names_phones_dict[line[0]] = int(line[1])

current_query_name = 0
while True:
    try:
        current_query_name = input()
        if current_query_name:
            if names_phones_dict.get(current_query_name, 0) != 0:
                print(f"{current_query_name}={names_phones_dict[current_query_name]}")
            else:
                print("Not found")
    except:
        break
