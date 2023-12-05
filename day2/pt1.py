# Rules:
# Games have an upper limit of 12 red, 13 green and 14 blue.
# Take the sum of the IDs of each game that don't break the upper limits.

cube_limits = {
    "green": 13,
    "blue": 14,
    "red": 12,
}

sum = 0
with open("data.txt") as file:
    id = 1
    for line in file.readlines():
        shouldIncludeSum = True

        reveal_start_index = line.index(":") + 1
        reveals = line[reveal_start_index:].split(";")

        for reveal in reveals:
            draws = reveal.split(",")
            for draw in draws:
                [_, n, color] = draw.split(" ")
                color = color.replace("\n", "")
                if int(n) > cube_limits[color]:
                    shouldIncludeSum = False

        if shouldIncludeSum:
            sum += id

        id += 1
print(sum)