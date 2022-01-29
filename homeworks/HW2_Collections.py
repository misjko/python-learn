from random import randrange, choice
from string import ascii_lowercase

# create list of dicts with random letter-number key-values
random_dict_list = [{choice(ascii_lowercase): randrange(0, 99) for j in range(randrange(0, 25))}
                    for i in range(randrange(1, 9))]
print("Initial dicts in list:")
print(*random_dict_list, sep="\n")

# transform dict to {key: *{value: dataset number}} view
transformed_dict = {}
for key in set().union(*random_dict_list):
    transformed_dict[key] = {}
    for single_dict in random_dict_list:
        if key in single_dict:
            transformed_dict[key][single_dict[key]] = random_dict_list.index(single_dict)
print(f"Transformed dict: {transformed_dict}")

# merge dictionary
merged_dict = {}
for key in transformed_dict.keys():
    if len(transformed_dict[key]) == 1:
        merged_dict[key] = list(transformed_dict[key].keys())[0]
    else:
        values = transformed_dict[key]
        max_value = max(value for value in values)
        key = key + '_' + str(values[max_value])
        merged_dict[key] = max_value
print(f"Merged dict: {merged_dict}")
