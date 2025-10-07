# Program to check if one string is a substring of another

main_string = "Mainflow Internship"
sub_string = "Intern"

if sub_string in main_string:
    print("Yes,", sub_string, "is a substring of", main_string)
else:
    print("No,", sub_string, "is not a substring of", main_string)
