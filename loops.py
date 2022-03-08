i = 0
while i < 30:
	print(i)
	i+=1
#q1
print("Hi, welcome to Ice Cream Maker.")
order_complete = False 
toppings_list = []
topping_count = 0
toppings_avaliable = ["vanilla", "strawberry", "chocolate", "sprinkles", "nuts", "raisins", "chocolate suace", "flake", "m&ms"]

print("We have the toppings")
print(*toppings_avaliable)

while order_complete == False:
	
	topping = input("What topping from the lsit would you like? push enter to finish\n")
	if topping == "" or topping_count == 6:
		print("order done")
		order_complete = True
	elif topping in toppings_list:
		print("You already have that topping")
	elif topping.lower() == "vanilla": 
		print("Great, adding it to the list")
		toppings_list.append(topping)
		topping_count +=1
	elif topping.lower() == "strawberry": 
		print("Great, adding it to the list")
		toppings_list.append(topping)
		topping_count +=1
	elif topping.lower() == "chocolate": 
		print("Great, adding it to the list")
		toppings_list.append(topping)
		topping_count +=1
	elif topping.lower() == "sprinkles": 
		print("Great, adding it to the list")
		toppings_list.append(topping)
		topping_count +=1
	elif topping.lower() == "nuts": 
		print("Great, adding it to the list")
		toppings_list.append(topping)
		topping_count +=1
	elif topping.lower() == "raisins": 
		print("Great, adding it to the list")
		toppings_list.append(topping)
		topping_count +=1
	elif topping.lower() == "chocolate suace": 
		print("Great, adding it to the list")
		toppings_list.append(topping)
		topping_count +=1
	elif topping.lower() == "flake": 
		print("Great, adding it to the list")
		toppings_list.append(topping)
		topping_count +=1
	elif topping.lower() == "m&ms": 
		print("Great, adding it to the list")
		toppings_list.append(topping)
		topping_count +=1
	else:
		print("Sorry but that topping is not avaliable")

print("Here are your toppings")
print(*toppings_list,sep = "\n")



