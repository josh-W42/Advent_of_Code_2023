import re

data = []
with open("./data.txt") as file:
    data = [re.sub(r'[^0-9]', repl="", string=x) for x in file.readlines()]
print(sum([int(x[0] + x[len(x) - 1]) for x in data if len(x) > 0]))
