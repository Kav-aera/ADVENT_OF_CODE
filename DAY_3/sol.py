# def process_string(input_str):
#     """
#     Process a string containing mul instructions and return the sum of all valid multiplications.
#     Valid format is: mul(x,y) where x and y are integers
    
#     Args:
#         input_str (str): The input string containing mul instructions
        
#     Returns:
#         int: Sum of all valid multiplications
#     """
#     sum_total = 0
#     pos = 0
    
#     while True:
#         # Find next "mul("
#         try:
#             pos = input_str.index("mul(", pos)
#         except ValueError:
#             break
            
#         start = pos + 4  # Skip "mul("
#         if start >= len(input_str):
#             break
            
#         # Count opening and closing parentheses to handle nesting
#         paren_count = 1
#         end = start
        
#         while end < len(input_str) and paren_count > 0:
#             if input_str[end] == '(':
#                 paren_count += 1
#             if input_str[end] == ')':
#                 paren_count -= 1
#             if paren_count > 0:
#                 end += 1
                
#         if paren_count == 0:
#             # Extract the substring between parentheses
#             nums = input_str[start:end]
            
#             # Find the comma
#             if ',' in nums:
#                 # Split and take only first two parts
#                 parts = nums.split(',', 1)  # Split at first comma only
#                 if len(parts) == 2:
#                     num1_str, num2_str = parts
                    
#                     # Strip any whitespace
#                     num1_str = num1_str.strip()
#                     num2_str = num2_str.strip()
                    
#                     # Check if strings contain valid numbers
#                     if (num1_str.isdigit() and num2_str.isdigit()):
#                         num1 = int(num1_str)
#                         num2 = int(num2_str)
#                         sum_total += num1 * num2
            
#             pos = end + 1  # Move past the current multiplication
#         else:
#             pos = start  # Move past the current invalid mul instruction
            
#     return sum_total

# def process_file(file_path):
#     """
#     Read and process a file containing mul instructions.
    
#     Args:
#         file_path (str): Path to the input file
        
#     Returns:
#         tuple: (result, error_message)
#     """
#     try:
#         with open(file_path, 'r') as file:
#             # Read the entire file content
#             content = file.read()
            
#             # Process the content
#             result = process_string(content)
#             return result, None
            
#     except FileNotFoundError:
#         return None, f"Error: Could not find file at {file_path}"
#     except PermissionError:
#         return None, f"Error: No permission to read file at {file_path}"
#     except Exception as e:
#         return None, f"Error: An unexpected error occurred: {str(e)}"

# def main():
#     file_path = r"c:\PROJECTS\ADVENT_OF_CODE\DAY_3\input.txt"
    
#     # Process the file
#     result, error = process_file(file_path)
    
#     # Handle the result
#     if error:
#         print(error)
#     else:
#         print(f"The result of processing the file is: {result}")

# if __name__ == "__main__":
#     main()
from operator import mul; import re
# print(eval('+'.join(re.findall(r'mul\(\d+,\d+\)', open('c:\PROJECTS\ADVENT_OF_CODE\DAY_3\input.txt').read()))))
d = open('c:\PROJECTS\ADVENT_OF_CODE\DAY_3\input.txt').read()
for s in d, re.sub(r'don\'t\(\)[\s\S]*?(do\(\)|$)', '', d):
    print(eval('+'.join(re.findall(r'mul\(\d+,\d+\)', s))))