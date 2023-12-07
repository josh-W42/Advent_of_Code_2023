# PART 2

data = []
with open("data.txt") as file:
  data = [x.strip() for x in file.readlines()]

card_counts = {}
for row in data:
  [card, numbers] = row.split(":")

  temp = card.split(" ")
  card_num = int(temp[len(temp) - 1])
  if not card_counts.get(card_num):
    card_counts[card_num] = 1

  [winning_numbers, choices] = numbers.split("|")
  winning_numbers = winning_numbers.split(" ")
  choices = choices.split(" ")
  
  winning_numbers = [x for x in winning_numbers if x]
  choices = [x for x in choices if x]

  correct_choices = [x for x in choices if x in winning_numbers]

  for i in range(1, len(correct_choices) + 1):
    if card_counts.get(card_num + i):
      card_counts[card_num + i] += card_counts[card_num]
    else:
      card_counts[card_num + i] = 1 + card_counts[card_num]

print(sum(card_counts.values()))
