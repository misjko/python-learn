from random import randrange

# create list of random values
random_list = []
for i in range(100):
    random_list.append(randrange(1001))

# sort list in asc order
sorted_count = 1
while sorted_count > 0:
    sorted_count = 0
    for i in range(len(random_list) - 1):
        if random_list[i] > random_list[i+1]:
            temp = random_list[i+1]
            random_list[i+1] = random_list[i]
            random_list[i] = temp
            sorted_count = sorted_count + 1
print(random_list)

# calculate average for even and odd numbers
sum_odd = 0
count_odd = 0
sum_even = 0
count_even = 0
for i in range(len(random_list)):
    if (random_list[i] % 2) == 0:
        sum_even = sum_even + random_list[i]
        count_even = count_even + 1
    else:
        sum_odd = sum_odd + random_list[i]
        count_odd = count_odd + 1
print(f"Average for odd numbers is {sum_odd/count_odd}")
print(f"Average for even numbers is {sum_even/count_even}")
