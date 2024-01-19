#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
'Thirty'
'Days'
'Of'
'Python'
message = ' Thirty ' + ' Days ' + ' Of ' + ' Python '
print(message)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
'Coding'
'For'
'All'
message = ' Coding ' + ' For ' + ' All '
print(message)

#Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper)

#Change all the characters to lowercase letters using lower() method.
print(company.lower)

#Use capitalize(), title(), swapcase() methods to format the 'value' of the string Coding For All.
print(company.capitalize) 
print(company.swapcase)

#Cut(slice) out the first word of Coding For All string.
print(company[0:6])  

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))   

#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

#Change Python for Everyone to Python for All using the replace method or other methods.
message = 'Python for Everyone'
print(message.replace('Everyone', 'All'))

#Split the string 'Coding For All' using space as the separator (split()) .
message = 'Coding For All'
print(message.split( ))

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
message = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(message.split(','))

#What is the character at index 0 in the string Coding For All.
message = 'Coding For All'
print(message[0]) or print(message[0:1])

#What is the last index of the string Coding For All.
message = 'Coding For All'
print(message[0:14])

#What character is at index 10 in "Coding For All" string.
message = 'Coding For All'
print(message[0:10]) or print(message[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
#Create an acronym or an abbreviation for the name 'Coding For All'.
#Use index to determine the position of the first occurrence of C in Coding For All.

#Use index to determine the position of the first occurrence of F in Coding For All.
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#Does ''Coding For All' start with a substring Coding?
#Does 'Coding For All' end with a substring coding?
'   Coding For All      '  , remove the left and right trailing spaces in the given string.
#Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
#Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
#Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
#Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144