

import random
import time

start_time = time.time()
n = 10000
# list_to_be_sorted = [random.randint(0, 99) for x in range(n)]
sort_me = []
for x in range(n):
    sort_me.append(random.randint(0, 99))

swapped = True
while swapped:
    # Keep track of if swapped
    swapped = False
    # Checks each index
    for i in range(len(sort_me)-1):
        # if current > next index : swap elements
        if sort_me[i] > sort_me[i+1]:
            sort_me[i], sort_me[i+1] = sort_me[i+1], sort_me[i]
            swapped = True
    # If swapped is still false, list is sorted

end_time = time.time()
print(f"bubble sort took {end_time - start_time} seconds")
