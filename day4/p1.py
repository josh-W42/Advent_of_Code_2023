# PART 1
# points_for_one_card = 2^n-1 where n is the number of correct choices.
# Then take the sum of all the points_for_one_card

data = []
with open("data.txt") as file:
  data = [x.strip() for x in file.readlines()]

answer = 0
for row in data:
  [card, numbers] = row.split(":")
  [winning_numbers, choices] = numbers.split("|")
  winning_numbers = winning_numbers.split(" ")
  choices = choices.split(" ")
  
  winning_numbers = [*filter(lambda x: x, winning_numbers)]
  choices = [*filter(lambda x: x, choices)]
  
  correct_choices = [x for x in choices if x in winning_numbers]
  if len(correct_choices) > 0:
    answer += 2**(len(correct_choices) - 1)

    

print(answer)
