encoded_string =input("enter the string:")
components = list(filter(None, encoded_string.split('0')))
first = components[0]
last = components[1]
id = components[2]

