'''
#q1
order = int(input("How many ice creams would you like?\n"))
if order > 20:
	print("Sorry, there isn't enough ice cream left\n")
if order < 20:
	print(f"Here are your {order} ice creams.\n")

#q2
distance = int(input("Please enter how many km you are going to travel on your trip\n"))
if order > 200:
	print("Remember to fill up on fuel before your trip\n")
if order <= 200:
	print(f"You have enought fuel to last {distance}km\n")
else:
	print("Please neter a valid response\n")
#q3
age = int(input("Please enter your age\n"))
if age >= 18:
	print("You are now considered an adult\n")
if age < 18:
	print("You are still considered a minor")
#q4
movie = input("Please enter your favourite movie\n")
if movie.lower() == "lord of the rings":
	print("You have excellent taste\n")
if movie.lower() == "django":
	print("You have excellent taste\n")
else:
	print("There are better movies.")
#q5
tale = input("Have you heard the tale of Darth Plagueis the Wise? (yes or no)\n")
if tale.lower() == "yes":
	print("You must be a fan\n")
if tale.lower() == "no":
	print("Plagueis, the legend went, was so powerful and so wise he could use the Force to influence the midi-chlorians to create life, and even saved others from dying. He became so powerful, the only thing that he was afraid of was losing his power. His apprentice killed him in his sleep. What made it a tragedy was the irony that he could not save himself from his death, despite being able to save others.")
#q6
passionofchrist = input("Who directed Passion of Christ?\n")
if passionofchrist.lower() == "mel gibson":
	print("Correct\n")
else:
	print("Wrong. Mel Gibson did.\n")
'''
#q7
user_score = 0
game_show = input("Do you want to play a game?\n")
if game_show.lower() == "no":
	print("Okay then, see you later\n")
if game_show.lower() == "yes":
 user_name = input("Please enter your name.\n")
 print(f"Welcome {user_name}. You have decided to participate in a game show. The aim of the game is to answer the the most amount of questions correctly. If you beat the other contestants you will win $100,000.\n")
 print(f" You will be competing against Susan, Mark and John.\n")
 print("Question numero uno. How many times can you fit 5 into 25?\n")
 q1 = input(" (A) Four times. (B) Once. (C) Five times. (D) None of the above\n")
 if q1.lower() == "a":
 	print(f"Incorrect. Sorry {user_name}, but you've missed out on $100,000\n")
 elif q1.lower() == "c":
  print(f"Congratulations {user_name}. You're onto round number 2\n")
  user_score = user_score + 1
 elif q1.lower() == "b":
  print(f"Incorrect. Sorry {user_name}, but you've missed out on $100,000")
 elif q1.lower() == "d":
  print(f"Incorrect. Sorry {user_name}, but you've missed out on $100,000")
 print(user_score) 
# Due to time boundries, I've been unable to complete the game and am moving onto next task