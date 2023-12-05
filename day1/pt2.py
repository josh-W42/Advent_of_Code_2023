import re

word_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

data = []
with open("data.txt") as file:
    for line in file.readlines():
        sorted_tuples = []
        for key in word_dict.keys():
            found_index = line.find(key)
            if found_index >= 0:
                sorted_tuples.append((found_index, key))
                sorted_tuples.sort(key=lambda index_tuple: index_tuple[0])

        for index, key in sorted_tuples:
            line = re.sub(key, repl=f'{word_dict[key]}{key}', string=line)
        data.append(re.sub(r'[^0-9]', repl="", string=line))

sum = 0
for row in data:
    if len(row) > 0:
        sum += int(row[0] + row[len(row) - 1])

print(sum)
