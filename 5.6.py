#q1
money = 200
belt = 15
hat = 20
top = 30
pants = 40
shoes = 60
print(f"You have ${money}")
print(f"A hat costs ${hat}, belts cost ${belt}, tops cost ${top}, pants cost ${pants} and shoes cost 4{shoes}")
buying = input("What would you like to buy?\n")
if buying == "hat":
	money -= 20
	print(f"you have ${money} left")
if buying == "belt":
	money -= 15
	print(f"you have ${money} left")
if buying == "top":
	money -= 30
	print(f"you have ${money} left")
if buying == "pants":
	money -= 40
	print(f"you have ${money} left")
if buying == "shoes":
	money -= 60
	print(f"you have ${money} left")
if buying == "nothing":
	money == 200
	print(f"you have ${money} left")