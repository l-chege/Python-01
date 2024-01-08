  #string concatenation
print("20 days are " + str(20) + " minutes")
print(f"20 days are {20} minutes")
print(f"50 days are {50 * 24 * 60} minutes")

#variables
to_minutes = 24 * 60
print(f"20 days are {20 * to_minutes} minutes")

calculation_to_units = 24 
name_of_unit = "hrs"

print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
print(f"50 days are {50 * calculation_to_units} {name_of_unit}")

#functions
def days_to_units():
    print(f"20 days are {20 * calculation_to_units} {name_of_unit}")

days_to_units()

#function parameters
def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")

days_to_units(35)
days_to_units(20)
days_to_units(50)

#multiple input parameters  
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)

days_to_units(35, "Awesome!")
days_to_units(20, "Looks good!")

#scope of variables
def scope_test(num_of_days):
    my_var = "variable inside function"
    print(name_of_unit)   #global variable scope
    print(num_of_days)   #local variable scope
    print(my_var)   #local variable scope

scope_test(35)