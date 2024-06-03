try:
    my_list = [1, 2, 3, 4, 5]
    index = int(input("Enter the index you want to access: "))
    result = my_list[index]

except IndexError:
    print("Index is out of range!")

except ValueError:
    print("Please enter a valid integer index!")
