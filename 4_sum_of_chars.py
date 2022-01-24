number_of_lines = int(input())
sum_of_chars = 0
for number in range(number_of_lines):
    char = ord(input())
    sum_of_chars += char

print(f"The sum equals: {sum_of_chars}")
