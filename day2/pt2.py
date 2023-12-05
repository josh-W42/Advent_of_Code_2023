# Part 2
# Goal:
#   Find the minimum set of cubes that must be present.
#       Another way of looking at it is, what's the maximum number of cubes shown
#       for each cube.
#   Get the power of that set.
#   Find the sum of all minimum set powers.

sum = 0
with open("data.txt") as file:
    for line in file.readlines():
        reveal_start_index = line.index(":") + 1
        reveals = line[reveal_start_index:].split(";")

        max_cubes = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }

        for reveal in reveals:
            draws = reveal.split(",")
            for draw in draws:
                [_, n, color] = draw.split(" ")
                color = color.replace("\n", "")

                if int(n) > max_cubes[color]:
                    max_cubes[color] = int(n)

        sum += (lambda x, y, z: x * y * z)(*max_cubes.values())

print(sum)