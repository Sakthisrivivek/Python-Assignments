def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
            return line_count
    except FileNotFoundError:
        return "File not found"

file_path = 'demo.txt'
result = count_lines(file_path)
print("Number of lines:", result)
