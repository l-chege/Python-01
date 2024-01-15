from datetime import datetime                     #importing datetime module from datetime package

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

#calculate how many days from now till deadline
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")    #strptime() is a built-in function that converts a string to a datetime object
today_date = datetime.today()                              #today() is a built-in function that returns the current local date
time_till = deadline_date - today_date                               #subtracting two datetime objects gives a timedelta object

hours_till = int(time_till.total_seconds() / 60 / 60)                #total_seconds() is a built-in function that returns the total number of seconds in a timedelta object
print(f"Dear user! Time remaining for your goal: {goal} is {hours_till} hours")                                   
