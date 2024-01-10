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

#return value statement
def days_to_units(num_of_days):                                                                   #function is executed when called
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
                                                                                                  #return value is assigned/stored to variable 
my_var = days_to_units(20)
print(my_var)                                                                                     #variable is printed

#scope of variables
def scope_test(num_of_days):
    my_var = "variable inside function"
    print(name_of_unit)   #global variable scope
    print(num_of_days)   #local variable scope
    print(my_var)   #local variable scope

scope_test(35)

#user input validation - if.....else conditional statement
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
   
    
#encapsulation     #nested loop (loop inside a loop)
def validate_and_execute():
    if user_input.isdigit():                                                                #isdigit() is a built-in function to check if the input is a number
        user_input_number = int(user_input)
        if user_input_number > 0:       
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
    else:                                                                                  #if the input is not a number, the program will print the following message
        print("Your input is not a valid number. Don't ruin my program!")

user_input = input("Hey user, enter number of days and I will convert it to hrs! \n")            #user-input built-in function
validate_and_execute()

#exception error handling with try/except
def validate_and_execute():
    try: 
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program!")


user_input = input("Hey user, enter number of days and I will convert it to hrs! \n")
validate_and_execute()





    