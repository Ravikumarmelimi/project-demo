# PSET6
# Write a python script that reads the 
# first and last name of a person 
# and returns the full name.
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
full_name = first_name + " " + last_name
print("Full Name is: {} {}".format(first_name,last_name)) #using .format method
print("Full Name is: ", " ".join([first_name,last_name])) # using .join method
print('Full Name is: ', full_name)     # using + operator
