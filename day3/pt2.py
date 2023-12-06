# Part 2
# Goal find the sum of all gear ratios. A gear ratio occurs when a "*" is between 2 numbers.

data = []
with open("data.txt") as file:
    data = [x.strip() for x in file.readlines()]


def test(val: str):
    return val.isdigit()


gear_ratio_sum = 0
for i, row in enumerate(data):
    for j, s in enumerate(row):
        # We only care if we find a gear
        if s == '*':
            # Check all positions
            # Left would be data[i][j - 1]
            # Right would be data[i][j + 1]
            # Top would be data[i - 1][j]
            # Bottom would be data[i + 1][j]
            # DiagTopLeft would be data[i - 1][j - 1]
            # DiagBottemLeft would be data[i + 1][j - 1]
            # DiagTopRight would be data[i - 1][j + 1]
            # DiagBottomRight would be data[i + 1][j + 1]

            def find_other_digits(start_y: int, start_x: int) -> int:
                """
                Given a starting position in the variable data, finds all other digits to the left and right of it and
                joins them.

                *Ensure start_y is not out of range before calling this*

                :param start_y: The starting y index of the first digit. (The index of the row in data)
                :param start_x: The starting x index of the first digit. (The index in the string within the row)
                :return: The entire number cast as an int.
                """
                whole_number = data[start_y][start_x]
                index = start_x + 1
                # Go right first
                while index < len(row) and data[start_y][index].isdigit():
                    whole_number += data[start_y][index]
                    index += 1

                index = start_x - 1
                # Now go left
                while index >= 0 and data[start_y][index].isdigit():
                    whole_number = data[start_y][index] + whole_number
                    index -= 1

                return int(whole_number)


            part_pair = { }
            # Ensure we do not trigger out of bounds
            if i - 1 >= 0 and test(data[i - 1][j]):
                # Top would be data[i - 1][j]
                part_pair[find_other_digits(i - 1, j)] = True

            if j - 1 >= 0 and test(data[i][j - 1]):
                # Left would be data[i][j - 1]
                part_pair[find_other_digits(i, j - 1)] = True

            if i - 1 >= 0 and j - 1 >= 0 and test(data[i - 1][j - 1]):
                # DiagTopLeft would be data[i - 1][j - 1]
                part_pair[find_other_digits(i - 1, j - 1)] = True

            if i + 1 < len(data) and test(data[i + 1][j]):
                # Bottom would be data[i + 1][j]
                part_pair[find_other_digits(i + 1, j)] = True

            if j + 1 < len(row) and test(data[i][j + 1]):
                # Right would be data[i][j + 1]
                part_pair[find_other_digits(i, j + 1)] = True

            if i + 1 < len(data) and j + 1 < len(row) and test(data[i + 1][j + 1]):
                # DiagBottomRight would be data[i + 1][j + 1]
                part_pair[find_other_digits(i + 1, j + 1)] = True

            if i - 1 >= 0 and j + 1 < len(row) and test(data[i - 1][j + 1]):
                # DiagTopRight would be data[i - 1][j + 1]
                part_pair[find_other_digits(i - 1, j + 1)] = True

            if i + 1 < len(data) and j - 1 >= 0 and test(data[i + 1][j - 1]):
                # DiagBottemLeft would be data[i + 1][j - 1]
                part_pair[find_other_digits(i + 1, j - 1)] = True

            if len(part_pair) == 2:
                gear_ratio_sum += (lambda x, y: x * y)(*part_pair.keys())

print(gear_ratio_sum)
