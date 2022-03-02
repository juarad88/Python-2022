#q3
'''
key = input("please push any key then press enter.\n")
#q4
user_name = input("Please enter your name then press enter\n")
#q5
user_age = input(f"please enter your age then press enter, {user_name}\n")
#Q6
favourite_movie = input(f"{user_name} who is {user_age} years old, please enter your favourite movie\n")
#q7
book = input(f"{user_name} who is {user_age} years old, please enter your the name of a book\n")
#q8
adjective = input(f"{user_name} who is {user_age} years old, please enter an adjective\n")
#q9
noun = input(f"{user_name} who is {user_age} years old, please enter a noun\n")
#q10
verb = input(f"{user_name} who is {user_age} years old, please enter a verb\n")
#q11
word = input(f"{user_name} who is {user_age} years old, please enter your favourite word\n")
school = input(f"{user_name} who is {user_age} years old, please enter your school\n")
print(f"Hello {user_name}. I know a lot about you now. For example, you are {user_age} years old, your favourite movie is {favourite_movie}, you like the book {book}, an adjective, noun and verb you like to use is {adjective}, {noun} and {verb}. Your favourite word is {word}, and you go to {school}.\n")

#q12
age = int(input("How old are you?\n"))
#q13
print(f"In 10 years time, you will be {age +10}")
#q14
print(f"Because you are {age} years old, that means you were born either in the year {2022 - age} or the year {2021 - age}\n")
#q15
apples = int(input("How many apples do you have?\n"))
#q16
friends = int(input("How many friends do you have? (enter a number)\n"))
#q17
print(f" If you and your friends share your apples, you will each have {apples//friends} apples")
#q18
pizzas = int(input("How many pizzas would you like? (Enter a number)\n"))
#q19
people_eating = int(input("How many people will eat the pizzas? (Enter a number)\n"))
#q20
pizza_slices = pizzas * 8
print(f"When you all eat pizzas, you will each get {pizza_slices // people_eating} slices of pizza, and there will be {pizza_slices % people_eating} slices of pizza left.\n")
'''
#q21
user_money = int(input("How much money do you have? (Enter a number)\n"))
#q22
tv_cost = int(input("How much does a tv cost? (Enter a number)\n"))
#q23
if user_money >= tv_cost:
	print(f"If you buy a tv you will have ${user_money - tv_cost} left.\n")
if user_money <= tv_cost:
	print(f"Sorry you don't have enough money to buy a tv.\n")
if user_money == tv_cost:
	print("You have just the exact amount of money to be a tv\n")
#q24	
new_tvcost = tv_cost * 0.8
print(f"However, If you wait for a 20% discount on the tv, It will cost you ${new_tvcost}\n")
#q25
crypto_total = int(input("How much Crypto-coins do you own? (Enter a number)\n"))
cryptoindollars = crypto_total * 1.53
print(f"Your current crypto-coin collection has a networth of ${cryptoindollars}\n")