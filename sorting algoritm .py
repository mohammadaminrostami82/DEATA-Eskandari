import time


# Create a list of numbers
number_list = [11.6, -5, 45, -2.3, 66, -111, 123.5, 425 , 1425]


# Record the starting time
starting_time = time.time()

count = len(number_list)

# Implement the Bubble Sort algorithm to sort the list
for i in range(count):
    for l in range(0, count-i-1):
        if number_list[l] > number_list[l+1]:
            number_list[l], number_list[l+1] = number_list[l+1], number_list[l]

# Print the sorted list
print("Sorted Output:", number_list)

# Record the ending time
ending_time = time.time()

# Print the start and end times, as well as the total run time
print(f"You started your code at: {starting_time} and finished at: {ending_time}")
print("Your Run Time:", ending_time - starting_time)
