###############################
# https://github.com/Penjoor9/03230379_BIA101_CAP3
# Tshering Penjor
# BBI "B"
# 03230379
################################
# REFERENCES
# Links that you referred while solving 
# https://medium.com/@rajsigh717/python-interview-two-pointer-technique-5c4e3259a909
# https://towardsdatascience.com/two-pointer-approach-python-code-f3986b602640?gi=c32900e2f8b5
# http://link.to.an.article/video.com 
################################
# SOLUTION
# Your Solution Score:  493249
################################

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def extract_two_digit_number(line):
    start = 0
    end = len(line) - 1
    
    # Find the first digit
    while start < len(line) and not line[start].isdigit():
        start += 1
    
    # finding the first number
    while end >= 0 and not line[end].isdigit():
        end -= 1
    
    # check if digit are found
    if start < len(line) and end >= 0 and line[start].isdigit() and line[end].isdigit():
        return int(line[start] + line[end])
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

# solution
file_path = '379.txt' 
lines = read_input(file_path)
total_sum = calculate_sum_of_numbers(lines)
print_solution(file_path, total_sum)

