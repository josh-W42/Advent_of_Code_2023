# Par1
# Goal find the lowest location number that corresponds to an of the initial seeds.

data = []
with open("./day5/data.txt") as file:
  data = [x.strip() for x in file.readlines()]

starting_seeds = data[0].split(": ")[-1].split(" ")

# Note to self,
# The following will be considered inefficient
#   Storing all the mappings in memory.
#   Looping through the provided ranges. n is like in the hundred millions :D
# # For setup we can create dictionary maps for each destination and source.

# seed_to_soil = {}
# soil_to_fertilizer = {}
# fertilizer_to_water = {}
# water_to_light = {}
# light_to_temperature = {}
# temperature_to_humidity = {}
# humidity_to_location = {}

# # hmm
# mappings = [
#   seed_to_soil,
#   soil_to_fertilizer,
#   fertilizer_to_water,
#   water_to_light,
#   light_to_temperature,
#   temperature_to_humidity,
#   humidity_to_location,
# ]

# mapping_index = -1
# for row in data:
#   if row == '':
#     mapping_index += 1
#   elif row[0].isdigit():
#     # So... in each case here, we have the following 3 numbers
#     destination_start, source_start, delta_range = [int(x) for x in row.split()]
    
#     # Oh boy this is this inefficient huh?
#     for delta in range(delta_range):
#       mappings[mapping_index][source_start + delta] = destination_start + delta


# let's try a slightly different approach...
# instead of storing the exact mappings, we could just calculate the destination at the time when we need it?

# lets try to segment the data into related containers
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

mappings = [
  seed_to_soil,
  soil_to_fertilizer,
  fertilizer_to_water,
  water_to_light,
  light_to_temperature,
  temperature_to_humidity,
  humidity_to_location,
]

mapping_index = -1
for row in data:
  if row == '':
    mapping_index += 1
  elif row[0].isdigit():
    # Store the mappings sorted by the sources
    # Should have the following structure:
    #   [destination_start, source_start, delta_range]
    formatted_values = [int(x) for x in row.split()]
    mappings[mapping_index].append(formatted_values)
    mappings[mapping_index].sort(key=lambda x: x[1])



locations = []
for seed in starting_seeds:
  # map a seed to a fertilizer and fertilizer to a... all the way down to a location
  destination = 0
  source = int(seed)

  for mapping in mappings:
    for index, [destination_start, source_start, delta_range] in enumerate(mapping):
      if source >= source_start and source < source_start + delta_range:
        delta = source - source_start
        destination = destination_start + delta
        break
      elif index == len(mapping) - 1:
        destination = source
    source = destination
      
  # At this point the last destination is now our location
  locations.append(destination)


# Now find the lowest value in locations
print(min(locations))
