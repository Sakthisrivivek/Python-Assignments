def JtoI(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            corrected_content = content.replace('J', 'I')
            print(corrected_content)
    except FileNotFoundError:
        print("File not found")
JtoI("demo.txt")
