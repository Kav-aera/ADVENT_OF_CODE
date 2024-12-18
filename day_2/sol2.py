# def is_ascending(arr):
#     """Check if the array is in ascending order."""
#     for i in range(len(arr) - 1):
#         if arr[i] > arr[i + 1]:
#             return False
#     return True

# def is_descending(arr):
#     """Check if the array is in descending order."""
#     for i in range(len(arr) - 1):
#         if arr[i] < arr[i + 1]:
#             return False
#     return True

# def check_order(arr):
#     """Check if the report is safe by checking order and difference rules."""
#     for i in range(len(arr) - 1):
#         diff = abs(arr[i] - arr[i + 1])
#         if diff < 1 or diff > 3:  # The difference should be between 1 and 3
#             return False
#     return True

# def can_be_safe_by_removal(arr):
#     """Check if removing one element can make the report safe."""
#     for i in range(len(arr)):
#         # Create a new list by removing one element
#         temp = arr[:i] + arr[i+1:]
        
#         # After removing one element, check if the sequence is either ascending or descending
#         if (is_ascending(temp) or is_descending(temp)) and check_order(temp):
#             return True
#     return False  # No valid sequence found after removal

# def main():
#     # Open the input.txt file and read the contents
#     try:
#         with open("c:\PROJECTS\ADVENT_OF_CODE\DAY_2\input.txt", "r") as file:
#             count = 0
#             for line in file:
#                 # Convert the line into a list of integers
#                 report = list(map(int, line.split()))

#                 # Check if the report is safe or can be made safe by removal
#                 if check_order(report) or can_be_safe_by_removal(report):
#                     count += 1

#             print(f"Number of safe reports: {count}")

#     except FileNotFoundError:
#         print("Could not open input.txt file.")

# if __name__ == "__main__":
#     main()
def is_safe(local_diff_array):
    #print(local_diff_array)
    prev_diff = 0
    for i in range(0, len(local_diff_array)):
        abs_local_diff = abs(local_diff_array[i])
        if abs_local_diff < 1 or abs_local_diff > 3:
            return i
        if prev_diff == 0:
            prev_diff = local_diff_array[i]
            continue
        if (prev_diff > 0 > local_diff_array[i]) or (prev_diff < 0 < local_diff_array[i]):
            return i
    return -1

def add_and_check(local_diff_array, check_index, side):
    a = check_index if side == "left" else check_index + 1
    b = check_index - 1 if side == "left" else check_index
    new_val = local_diff_array[a] + local_diff_array[b]
    new_list = local_diff_array.copy()
    new_list.pop(a)
    new_list[b] = new_val
    return is_safe(new_list)

puzzle_input_file = open("c:\PROJECTS\ADVENT_OF_CODE\DAY_2\input.txt", "r")

nb_safe = 0
for line in puzzle_input_file:
    safe = True
    diff_array = []
    tokens = list(map(int, line.split()))
    for i in range(1, len(tokens)):
        diff_array.append(tokens[i] - tokens[i-1])
    last_index = len(diff_array) - 1
    check = is_safe(diff_array)
    if check > -1:
        if (check <= 1 and is_safe(diff_array[1:]) < 0) or (check == last_index and is_safe(diff_array[:-1]) < 0):
            safe = True
        elif check == 0 or add_and_check(diff_array, check, "left") > -1:
            if check == last_index:
                safe = False
            elif add_and_check(diff_array, check, "right") > -1:
                safe = False
    if safe:
        nb_safe = nb_safe + 1
print(nb_safe)