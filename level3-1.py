def read_even_length_strings(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            even_length_strings = [word for word in words if len(word) % 2 == 0]
            return ' '.join(even_length_strings)
    except FileNotFoundError:
        return "File not found"

file_path = 'doc.txt'
result = read_even_length_strings(file_path)
print(result)
