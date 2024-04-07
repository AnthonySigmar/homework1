# PPHA 30537
# Spring 2024
# Homework 1

# Sitong Guo
# AnthonySigmar

# Due date: Sunday April 7th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

#for example, a list as:
one_1 = [1,3,323,121,676]
for t in range(0, len(one_1)):
    print(f'The value at position {t+1} is {one_1[t]}')
    
#out:The value at position 1 is 1
#The value at position 2 is 3
#The value at position 3 is 323
#The value at position 4 is 121
#The value at position 5 is 676


# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.
list=["radar",
      "A man, a plan, a canal, Panama!",
              "Microsoft",
              "This isn't a palindrome"]
for w in list:
    w = w.lower()
    w= ''.join(bad for bad in w if bad.isalnum()) #isalnum() cited from https://www.w3schools.com/python/ref_string_isalnum.asp
    reverse = w[::-1]
    print(w == reverse)
    
#out:True True False False


# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']
choice = input('Please pick a vegetable I have available: ')

for choice in choice:
    if choice not in available_vegetables:
        print('you made invalid choice! Pick again!')
        choice = input('Please pick a vegetable I have available: ')
        next
    if choice in available_vegetables:
        print('now you have that!')
        break

# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.
list = ["Anaconda", "BinoMial", "Challenger", "drenCh", "Europa", "Frollo"]

result = [words.lower() for words in list if not (words.lower().startswith('a') 
                                                     or words.lower().startswith('b'))]
print(result)
#out:['challenger', 'drench', 'europa', 'frollo']

# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}
short_names = ['IL', 'IN', 'MI', 'WI']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']

dic = {short_names[i]: long_names[i] for i in range(len(short_names))}
print(dic)

#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]
def sums(a, b):
    sum = a + b
    if sum > 10:
        return 'big'
    elif sum == 10:
        return 'just right'
    else:
        return 'small'
    
result = []
for i,k in start_list:
    
    result.append(sums(i, k))    
print(result)
#Out:['just right', 'big', 'small', 'small', 'small']


# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 40
    return a + b
x = my_func()

#modified:
def my_func(a):
    b=40
    return a+b
x = my_func(10)
print(x)
# It does not need outlying global variable, easy to track down if there were bug. 
# It also becomes more reusable since you can assign value to the argument.


# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:
import random
#from numpy import random
def password(length, special_chars=True, numbers=True):
    if not 8 <= length <= 16:
        print('!WARNING! Password length must be between 8-16 characters.')
        return 'exit...'

    char = ''
    
    if numbers:
        char += '0123456789'
    if special_chars:
        char += '!@#$%^&*'
    char += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    return ''.join(random.choice(char) for i in range(length))

leng = int(input('input the lenth of your password:'))
word = password(leng)
print('generated:', word)
#out:L4!!6HacenLO2
  
# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.

class MovieDatabase:
    def __init__(self, creator):
        self.creator = creator
        
        self.movies = []

    def add_movie(self, moviename, genera, rating):
        self.movies.append({'name': moviename,
            'genera': genera,
            'ratings': rating})

    def what_to_watch(self):
        if not self.movies:
            print("No movie in store")
            return

        selectmovie = random.choice(self.movies)
        print(f"Greetings! My Lord {self.creator}, are your highness in the mood of watching this:")
        print(f"Name: {selectmovie['name']}")
        print(f"Genre: {selectmovie['genera']}")
        print(f"Rating: {selectmovie['ratings']} ☆ out of five ☆")


mov = MovieDatabase("tony")
mov.add_movie("wandering earth", "sci-fi", 4.9)
mov.add_movie("interstellar", "sci-fi", 5)
mov.add_movie("the dark knight", "superhero", 4.5)
mov.add_movie("pirate of the caribbeans", "fantasy", 4.4)

mov.what_to_watch()
#out:Greetings! My Lord tony, are your highness in the mood of watching this:
#Name: wandering earth
#Genre: sci-fi
#Rating: 4.9 ☆ out of five ☆
