################################
# Github Repo link
# Your Name
# Your Section 
# Your Student ID Number
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# http://link.to.an.article/video.com 
################################
# SOLUTION
# Your Solution Score: <total sum>
################################

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def extract_two_digit_number(line):
    first_digit = None
    last_digit = None
    
    # Find the first digit
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    
    # Find the last digit
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break
    
    # Form the two-digit number
    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    else:
        return 0

def calculate_sum_of_numbers(lines):
    total_sum = 0
    for line in lines:
        number = extract_two_digit_number(line)
        total_sum += number
    return total_sum

def print_solution(file_name, total_sum):
    print(f"The total sum of from the given input file {file_name} is {total_sum}")

# Main execution
file_path = '379.txt'
lines = read_input(file_path)
total_sum = calculate_sum_of_numbers(lines)
print_solution(file_path, total_sum)

