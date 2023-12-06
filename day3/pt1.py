# Part 1
# Goal find the sum of all numbers adjacent to a symbol

data = []
with open("data.txt") as file:
    data = [x.strip() for x in file.readlines()]


def test(val: str):
    return val != '.' and not val.isdigit()

part_nums = []
for i, row in enumerate(data):
    digit_segment = ''
    segment_is_adjacent = False
    for j, s in enumerate(row):
        if s == '.' and segment_is_adjacent:
            part_nums.append(int(digit_segment))
            digit_segment = ''
            segment_is_adjacent = False
        elif s == '.':
            digit_segment = ''
            segment_is_adjacent = False
        elif s.isdigit():
            digit_segment += s

            # if this is the end of the row...
            if j == len(row) - 1 and segment_is_adjacent:
                part_nums.append(int(digit_segment))
                continue

            # if we've already determined that the segment is adjacent to a symbol...
            if segment_is_adjacent:
                continue

            # Check all positions
            # Left would be data[i][j - 1]
            # Right would be data[i][j + 1]
            # Top would be data[i - 1][j]
            # Bottom would be data[i + 1][j]
            # DiagTopLeft would be data[i - 1][j - 1]
            # DiagBottemLeft would be data[i + 1][j - 1]
            # DiagTopRight would be data[i - 1][j + 1]
            # DiagBottomRight would be data[i + 1][j + 1]

            # Ensure we do not trigger out of bounds
            if i - 1 >= 0 and test(data[i - 1][j]):
                # Top would be data[i - 1][j]
                segment_is_adjacent = True

            if j - 1 >= 0 and test(data[i][j - 1]):
                # Left would be data[i][j - 1]
                segment_is_adjacent = True

            if i - 1 >= 0 and j - 1 >= 0 and test(data[i - 1][j - 1]):
                # DiagTopLeft would be data[i - 1][j - 1]
                segment_is_adjacent = True

            if i + 1 < len(data) and test(data[i + 1][j]):
                # Bottom would be data[i + 1][j]
                segment_is_adjacent = True

            if j + 1 < len(row) and test(data[i][j + 1]):
                # Right would be data[i][j + 1]
                segment_is_adjacent = True

            if i + 1 < len(data) and j + 1 < len(row) and test(data[i + 1][j + 1]):
                # DiagBottomRight would be data[i + 1][j + 1]
                segment_is_adjacent = True

            if i - 1 >= 0 and j + 1 < len(row) and test(data[i - 1][j + 1]):
                # DiagTopRight would be data[i - 1][j + 1]
                segment_is_adjacent = True

            if i + 1 < len(data) and j - 1 >= 0 and test(data[i + 1][j - 1]):
                # DiagBottemLeft would be data[i + 1][j - 1]
                segment_is_adjacent = True

            if j == len(row) - 1 and segment_is_adjacent:
                part_nums.append(int(digit_segment))
                digit_segment = ''
                segment_is_adjacent = False

        elif segment_is_adjacent:
            # This is the case where s is a symbol and a segment of nums are adjacent to a symbol
            part_nums.append(int(digit_segment))
            digit_segment = ''
            segment_is_adjacent = False

print(sum(part_nums))
