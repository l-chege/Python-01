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
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program!")

#while loop stop execution 
user_input = ""              # assign an empty string to user_input
while user_input != "exit":        #loop breaks and stops program (condition gets evaluated)
    user_input = input("Hey user, enter number of days as a comma separated list and I will convert it to hrs! \n")        #user is  prompted for its input #function is called & input is validated and executed.
    list_of_days = user_input.split(", ")        #split() is a built-in function that splits a string into a list

    print(list_of_days)
    print(set(list_of_days))        #set() is a built-in function that removes duplicate elements from a list

    print(type(list_of_days))       #type() is a built-in function that returns the type of an object
    print(type(set(list_of_days)))  
    
    """print(type(user_input.split(",")))
    print(user_input.split(","))  """      
    for num_of_days_element in user_input.split(", "):              #for loop iterates over each character in the user_input string
        validate_and_execute()      

"""#basic list operations
my_list = ["January", "February", "March"] 
print(my_list[0])                                       #accessing list elements

my_list.append("April")                                 #adding elements to list
print(my_list[3])"""


"""#basic set operations
my_set = {"January", "February", "March"}
for element in my_set:
    print(element)                                       

my_set.add("April")                                      #adding elements to set
print(my_set)
my_set.remove("January")                                 #removing elements from set
print(my_set)"""








    