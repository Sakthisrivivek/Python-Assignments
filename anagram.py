
string1 = input("Enter the string1: ")
string2=input("Enter the string2: ")
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are the same
if sorted(string1) == sorted(string2):
    print(f"Output:True")
elif sorted(string1) != sorted(string2):
    print(f"Output:False")