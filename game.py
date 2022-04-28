from adventurelib import *
import random
Room.items = Bag()
inventory = Bag()
#All new code goes here





#rooms
starting_room = Room(""" You look around and see a small wooden desk in one corner of the room, a bookshelf in another and a cupboard against one of the walls. In front of you is a door with some kind of lock on it.
	""")

store_room = Room(""" As you enter the room you see large old dusty crates stacked upon each other. You see a old wooden door with no lock.
	""")

weapon_room = Room(""" You walk inside the next room. Inside you see racks and racks filled with a large assortment of weapons. Swords, axes, spears and morningstars. Once again there is a door with no lock on it.
	""") 

twisted_caverns = Room(""" The door opens to a vast room with a goblin warrior guarding them. He appears to be holding some type of rusty dagger. Behind him is a open door
	""")

dark_pool = Room(""" After exiting the tunnel you enter a dark cave with some sunlight edging it's way onto the water. The sunlight is coming from too high up to escape that way. Through the clear water you see golwing blue lines leading to two diffetrent points. On one side th eline branches into three where they each lead to a glowing leaver. On the other side the line leads to a closed door.
	""")

Temple_of_Dumathion = Room(""" The door opens to a new body of water. You swim through and surface. In front of you is an acient door . Towering above is a hideous ork. He is holding a huge hammer in his hands. "Who dare get past the gate keeper?" He asks. Without waiting for an answer he rushes up to you pulling back his hammer.
	""")

tomb_entry = Room(""" After walking through the door you walk down a passage way enscribed with ancient language. You are able to make out some of it but not all. "Long ago there was a soldier.... Blessed by the godesss.....said to have magic powers..... Soldier buried here." You continue walking to see the walkway open into a big dusty tomb.
	""")
murials_tomb = Room(""" You walk into Murial's tomb. All on the walls a beautiful carvings, telling fo her legacy. Above the tomb is a statue of Murial. But there appers to be something missing. Around the statue's neck hangs a necklace but the famous red jewel is not there. Prehaps it is hidden somewhere? Maybe they just forgot to add it?
	""")

mirror_room = Room(""" After passing into the next room you see enormous panes of glass all angled differently. On the roof, sits a round orb like object. Through a gap in the roof slivers a single beam of light.
	""")

treasure_room = Room("""When entering the next room you freeze in awe. This room is filled with gold and jewels and shiny objects in every size possible. This much gold would make even a king look poor. Shame you can't carry it all
	""")

Wizard_lair = Room("""The door opens into a vast stone room. Stairs start to climb up reaching a huge throne high above the ground. On each side of the thorne flames flicker, lighting up the room. Sitting comfortabely on the throne is The wizard that killed you. He stands up then dissapears, reemerging in front of you. "Back again are we?" He asks. You tighten your grip on your weapon.
	""")

# Define items
gold_coin = Item("gold coin", "coin")
gold_coin.description = "The coin is made of gold. It's a bit dirty but you can make out a frog on one side. Weird coin"

paper_clip = Item("paper clip","paperclip")
paper_clip.description = "It's an ordinary paper clip"

beef_jerky = Item("dried beef jerky", "beef jerky", "jerky", "dried jerky")
beef_jerky.description = "The dried meat looks old but edible."

sword = Item("sword")
sword.description = "You take a sword. It's hilt is wrapped in a dark but soft leather. The pommel has a orange jewel embedded inside it. It's crossguard is shaped like a dragons wing on each side of the sword. The blade is double edged and appears very sharp. A good choice" 

axe = Item("axe", "double sided axe")
axe.description = "You pick up the axe inspecting it. It has a long handle that has enough room to weild with two hands. It is a double sided axe, with a spike on the top. The blades are big and the edges are extremely sharp. A brutes weapon"

spear = Item("spear")
spear.description = "You take a dangerous lookung spear. The spear is about 2 metres long. The handle is made of polished oak with cloth wrapped tightly around the shaft acting as a handle. The blade starts by curving outwards then coming back in to make a very sharp tip. A ranged weapon "

morningstar = Item("morningstar")
morningstar.description = "You pick up a mace. The handle is made of metal. Cloth is wrapped around to ensure the weapon doesn't fly out your hand when you swing it. The end of the mace is heavy and has sharp spikes coming out in all directions. A lethal weapon"








#Define bags
starting_room.items.add(gold_coin)
starting_room.items.add(paper_clip)
store_room.items.add(beef_jerky)
weapon_room.items.add(sword)
weapon_room.items.add(axe)
weapon_room.items.add(spear)
weapon_room.items.add(morningstar)

#variables
current_room = starting_room
door_opened = False
player_health = 100
goblin_health = 35
damage = 0
defend = 0
wizard_health = 175
player_damage = 0
player_defense = 0


#binds
@when("look")
@when("look around")
def look():
	global current_room
	print(current_room)

#takes item
@when("take ITEM")
@when("pick up ITEM")
@when("grab ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
		if item == "sword":
			print("After taking your weapon, All the other weapons disappear in a plume of smoke")
			current_room.items.take('axe')
			current_room.items.take('spear')
			current_room.items.take('morningstar')
		if item == "axe":
			print("After taking your weapon, All the other weapons disappear in a plume of smoke")
			current_room.items.take('sword')
			current_room.items.take('spear')
			current_room.items.take('morningstar')
		if item == "spear":
			print("After taking your weapon, All the other weapons disappear in a plume of smoke")
			current_room.items.take('axe')
			current_room.items.take('sword')
			current_room.items.take('morningstar')
		if item == "morningstar":
			print("After taking your weapon, All the other weapons disappear in a plume of smoke")
			current_room.items.take('axe')
			current_room.items.take('spear')
			current_room.items.take('sword')
	if item in inventory: #prints item discription
		f=inventory.find(item)
		print(f.description)
	#looks at clothes.
	elif item == "clothes":
		print("You take a closer look at the clothes but find they are too small to wear")
	#secret room
	elif item == "book":
		print("As you go to take a book off the shelf, you find that the book won't move. In frustration you pull on the book and it results in a low grumbling sound. After a few seconds the entire bookshelf has moved to one side, revealing a secret room")
		@when("enter")
		@when("enter secret room")
		@when("go intp secret room")
		def secret_room():
			print("""You enter the secret room. Inside is a wooden table filled with papers with some strange writting that you cannot read Holding them together is a paper clip""")
	else:
		print(f"You cannot take {item}")

#shows inventory	
@when("inventory")
@when("show inventory")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

#1st room
#looks at bookshelf
@when("look at bookshelf")
@when("search bookshelf")
@when("go to bookshelf")
@when("look at book shelf")
@when("search book shelf")
@when("go to book shelf")
def search_bookshelf():
	print("You walk over to the dusty bookshelf. On the racks are many books, some different sizes and colours")
#looks at cupboard
@when("go to cupboard")
@when("search cupboard")
@when("look at cupboard")
def search_cupboard():
	print("You go over to the cupboard . It is tall and made of a dark oak. You open it revealing some old clothes.")

#looks at desk
@when("go to desk")
@when("go to wooden desk")
@when("search desk")
@when("search wooden desk")
def search_desk():
	print("You walk up to the desk investigating it. The desk is rather small and made of smooth oak. On the desk sits a candle. The candle is the only light source in the room. The desk has a drawer that can be opened")
#opens drawer
@when("open drawer")
@when("search drawer")
@when("look in drawer")
@when("open draw")
@when("search draw")
@when("look in draw")
def seacrh_drawer():
	print("You open the drawer. Inside is a single gold coin")
#uses paperclip 
@when("use paper clip")
@when("use paperclip")
@when("unlock door")
@when("unlock door with paperclip")
@when("unlock door with paper clip")
@when("pick lock")

#player pciks lock to open door
def pick_lock():
	if inventory.find("paper clip") and current_room == starting_room:
		print("You go to the door and unfold the paper clip and insert it into the lock. After turning it around a few times you hear a soft click, and the lock is off.")	
		global door_opened
		door_opened = True
	else:
		print("You don't have the equipment to pick the lock")
		
		                         
#leaving rooms                       
@when("open door")
@when("go through door")
@when("exit room")
@when("exit")
@when("leave")
@when("leave room")
def exit_startingroom():
	global current_room
	if door_opened == True and current_room == starting_room:
		print("You go through the door and into the next room")
		current_room = store_room
		print(current_room)
	elif door_opened == True and current_room == store_room:
		print("You go through the door and into the next room")
		current_room = weapon_room
		print(current_room)
	elif door_opened == True and current_room == weapon_room:
		print("You go through the door and into the next room")
		current_room = twisted_caverns
		print(current_room)	
	#if player tries to leave room and goblin is still alive, they cannot.
	elif door_opened == True and current_room == twisted_caverns and goblin_health > 0:
		print("You cannot exit the room. The goblin is guarding all possible exits")
		current_room = twisted_caverns
	elif door_opened == True and current_room == twisted_caverns and goblin_health <= 0:
		print("After slaying the goblin you go through the door and into the next room")
		current_room = mirror_room
		print(current_room)	
	elif door_opened == True and current_room == mirror_room and goblin_health <= 0:
		print("You exit the mirror room.")
		current_room = Wizard_lair
		print(current_room)	
#player dies if they try to leave room and wizard is stilol alive
	elif door_opened == True and current_room == Wizard_lair and goblin_health <= 0 and wizard_health > 0:
		print("You turn around, running to the place where you entered. Unfortunately you don't get far. The wizard shoots a jagged blue bolt out of his staff, turing you into ash.")
		quit()
	else:
		print("The door is locked")



#player exits starting room
@when("exit secret room")
@when("leave secret room")
def exit_secret_room():
	global current_room
	if current_room == starting_room:
		print("You walk out of the secret room and into the main room.")
#2nd Room
#searches crates
@when("search crates")
@when("search crate")
@when("go to crates")
@when("look in crates")
@when("look inside of crates")
@when("look inside crates")
@when("open crate")
@when("open crates")
def search_crates():
	if current_room == store_room:
		print("You search the crates. Inside you find some dried beef jerky")
	else:
		print("there are no crates here")
#player eats jerky to gain 20 life. Life total caps at 100
@when("eat jerky")
@when("use jerky")
@when("eat  beef jerky")
@when("eat dried beef jerky")
@when("use beef jerky")
@when("use dried beef jerky")
def eat_jerky():
	if inventory.find("beef jerky"):
		global player_health
		if player_health < 100:
			player_health += 20
			print("You eat the jerky. It's tough but doesn't taste too bad") 
			if player_health >100:
				player_health = 100
		elif player_health > 100:
			player_health = 100
			print("You eat the jerky. It's tough but doesn't taste too bad")
		elif player_health == 100:
			print("Health is full")
			player_health = 100
		inventory.take("jerky")

#Shows player health
@when("player health")
@when("health")
@when("show player health")
@when("show health")
def show_health():
	global player_health
	if player_health >= 100:
		player_health =  100
	print(player_health)


#3rd room
#takes a closer look at the weapons
@when("search weapons")
@when("search racks")
@when("search weapon racks")
@when("inspect weapons")
@when("inspect racks")
@when("inspect weapon racks")
@when("go to weapons")
@when("go to racks")
@when("go to weapon racks")
def search_weapons():
	if current_room == weapon_room:
		print("You inspect the wepon racks. There are plenty of weapons to chose from. You are only strong enough to carry one weapon. What weapon will you chose? Axe, sword, spear or morningstar")


#4th room (1st fight)
@when("attack goblin")
@when("fight goblin")
@when("kill goblin")
@when("slay goblin")
@when(" hit goblin")
@when("attack goblin with sword")
@when("fight goblin with sword")
@when("kill goblin with sword")
@when("slay goblin with sword")
@when("hit goblin with sword")
@when("attack goblin with axe")
@when("fight goblin with axe")
@when("kill goblin with axe")
@when("slay goblin with axe")
@when("hit goblin with axe")
@when("attack goblin with spear")
@when("fight goblin with spear")
@when("kill goblin with spear")
@when("slay goblin with spear")
@when("hit goblin with spear")
@when("attack goblin with morningstar")
@when("fight goblin with morningstar")
@when("kill goblin with morningstar")
@when("slay goblin with morningstar")	
@when("hit goblin with morningstar")
def fight_goblin():
	if current_room == twisted_caverns:
		print("You swing at the goblin but it manages to dodge your attack just in time. The goblin stumbles back, off balance.")
		global goblin_health
		global player_health
		while goblin_health >= 1:
			choice = input("What will you do?\nAttack\nDefend\n")#gives player choice to either attack goblin or defend against ot 
			if choice.lower() == "attack":
				global damage
				damage = random.randint(1,10)#asigns random integer between 1 and 10 for attack
				#prints action based on outcome of the random integer (attack)
				if damage == 1:
					print("You miss. Your pathetic attack doesn't even graze your opponent, leaving you wide open")
					print("The goblin slashes at your body with his rusty dagger.")
					player_health -= 20
				if 2 <= damage <=4:
					print("You swing at the goblin, however, your swing is weak and doesn't do that much damage to the goblin")
					goblin_health -=10
					print("The goblin quickly recovers, slashing his dagger at you. The blade makes contact, producing a small wound")
					player_health -=5
				if 5 <= damage <= 7:
					print("You swing your weapon at the goblin. It hits him hard enough to make him stagger back")
					goblin_health -=15
					print("The goblin recovers again, and attacks. His attack is parried by your blade so that it only cuts your arm")
					player_health -=3
				if 8 <= damage <=9:
					print("You draw back your arm and swing at the goblin. It hit's him on the head causing a large amount of damage to it")
					goblin_health -=20
					print("The goblin shakes his head in recovery. He lunges at you with his dagger grazing your ribs.")
					player_health -=8
				if damage == 10:
					print("You launch your weapon at the goblin with all your strength. It hits him on the head producing a loud crunch. The goblin falls to the ground")
					goblin_health -=30
					print("The goblin stands up stunned")

			if choice.lower() == "defend":
				global defend
				defend = random.randint(1,10)#asigns random integer between 1 and 10 for defending
				#print scence based on outcome of random intger(defend)
				if defend == 1:
					print("The goblin slashes at your body with his rusty dagger. You parry the blade with your own.")
					print("Retaliating you swing your weapon at the goblin. It hits him hard in the ribs, piercing flesh making him whimper.")
					goblin_health -= 20
				if 2 <= defend <=4:
					print("The goblin strikes at you. You manage to block just in time for the blade to miss your body. However you were still hit in the arm.")
					print("Blocking the goblin's attack threw him off balance. He trips over a rock and hits the ground with a slap.")
					goblin_health -=2
					player_health -=2
				if 5 <= defend <= 7:
					print("The goblin turns around swinging his blade with enormous strength. You manage to lift your weapon up in time to block the blow. It's power hits your weapon out of your hands and sends you spiralling to the ground.")
					print("As you land on the ground, the golbin swings at you again, this time with less power. His blade slices through you leg producing blood. As he swings a second time you kick him in the face giving enough time to pick up your weapon and stand up.")
					goblin_health -=6
					player_health -=5
				if 8 <= defend <=9:
					print("The goblin charges at you ready to swing his dagger at your skull. You block the blade almost effortlessly, Then hit him in the chest with the blunt end of your weapon. ")
					goblin_health -=10
				if defend == 10:
					print("The goblin swings at you. You go to block but stumble over a rock throwing you off balance.")
					print("The goblin's attack hits you hard, producing a cut on the side of your head. ")
					player_health -=30
		else:#prints statement once player has killed the goblin
			print("You hit the goblin one final time. Blood starts spilling on the ground, forming a puddle around it's head.")
			print(f"Health remaining : {player_health}")

#5th room
#delfecting light off weapon to solve puzzle and leave room
@when("deflect light")
@when("deflect light with weapon")
@when("deflect light with sword")
@when("deflect light with spear")
@when("deflect light with axe")
@when("deflect light with morningstar")
@when("deflect light off weapon")
@when("deflect light off sword")
@when("deflect light off spear")
@when("deflect light off axe")
@when("deflect light off morningstar")
@when("bounce light off weapon")
@when("bounce light off sword")
@when("bounce light off spear")
@when("bounce light off axe")
@when("bounce light off morningstar")
def deflect_light():
	if current_room == mirror_room:
		print("You delfect the light beam using your weapon. After a few attempts you manage to shine the light on the orb, after a few seconds the orb starts to glow a pale green.")
		print("Thr room starts to rumble as a pane of glass ascends making way to a possible exit")

#boss fight
@when("attack wizard")
@when("fight wizard")
@when("kill wizard")
@when("slay wizard")
@when(" hit wizard")
@when("attack wizard with sword")
@when("fight wizard with sword")
@when("kill wizard with sword")
@when("slay wizard with sword")
@when("hit wizard with sword")
@when("attack wizard with axe")
@when("fight wizard with axe")
@when("kill wizard with axe")
@when("slay wizard with axe")
@when("hit wizard with axe")
@when("attack wizard with spear")
@when("fight wizard with spear")
@when("kill wizard with spear")
@when("slay wizard with spear")
@when("hit wizard with spear")
@when("attack wizard with morningstar")
@when("fight wizard with morningstar")
@when("kill wizard with morningstar")
@when("slay wizard with morningstar")	
@when("hit wizard with morningstar")
def fight_wizard():
	if current_room == Wizard_lair:
		print("The wizard  takes a step back twirling his staff in his hands, ready to strike.")
		global wizard_health
		global player_health
		while wizard_health >= 1:
			boss_fight = input("What will you do?\nAttack\nDefend\n")#gives player choice to either fight wizard or defend against him
			if boss_fight.lower() == "attack":
				global player_damage
				player_damage = random.randint(1,10)#asigns random integer between 1 and 10 for attack
				#prints scene based on outcom of random integer(attack)
				if player_damage == 1:
					print("You rush up to the wizard, swinging your weapon at him. The wizard teleports behind you swinging his weapon at the back of your head. The blow is powerfull and it sends you flying into the ground")
					print("You stand back up and face the wizard")
					player_health -= 25
				if 2 <= player_damage <=4:
					print("You swing your weapon at the wizard. He miscalculates his teleport and get's hit by your attack.")
					wizard_health -=10
					print("The wizard snarls in pain and returns with a backhanded attack. You pull you weapon up enough to weaken the blow.")
					player_health -=10
				if 5 <= player_damage <= 7:
					print("You attack the wizard. It hits him on his side, and the wizard falls to his knees")
					wizard_health -=15
					print("Recovering from the blow, the wizard sweeps your feet off the ground using his staff")
					player_health -=8
				if 8 <= player_damage <=9:
					print("You feint at the wizard catching him off guard, leaving him open. You switch the direction of your attack hitting him in the ribs")
					wizard_health -=20
					print("The wizard falls to the ground. He mutters a few words under his breath, then shouts. The force of his voice sends you soaring across the room. You land painfully on the ground")
					print("In agony you stand back up and face the wizard")
					player_health -=13
				if player_damage == 10:
					print("You throw your weapon at the wizard. The blunt end of the weapon hits the wizard on his head.")
					wizard_health -=30
					print("The wizard stands up stunned, and you retrieve your weapon")

			if boss_fight.lower() == "defend":
				global player_defense
				player_defense = random.randint(1,10)#creates random integer between 1 and 10 for defending
				#prints scene based on outcome of random integer (defend)
				if player_defense == 1:
					print("The wizard swings his staff at you. You parry the attack with your weapon.")
					print("Retaliating, you swing your weapon at the wizard. It hits him hard on the shoulder, piercing flesh making him yelp.")
					wizard_health -= 20
				if 2 <= player_defense <=4:
					print("You pull you weapon up just in time to partailly block the wiazards attack. The force still sends you staggering backwards.")
					print("The momentum of the wizards swing tips him off balance. You see an opining and send a knee flying into his stomach, making him double over")
					wizard_health -=8
					player_health -=5
				if 5 <= player_defense <= 7:
					print("The wizard teleports behind you hitting you hard on the back.")
					print("You fall to the ground with a grunt as you land. The wizard lifts his staff to strike again but you sweep his legs and stand back up")
					wizard_health -=6
					player_health -=10
				if 8 <= player_defense <=9:
					print("The wizards speaks a few words in a strange language. You interrupt his magic by smashing the back end of your weapon into his face")
					wizard_health -=10
				if player_defense == 10:
					print("The wizard aims his staff at you and whispers a few words. Out the end of the staff shoots a blue bolt of lightning")
					print("The bolt hits you in the body sending you skimming across the floor. You slowly get on your feet.")
					player_health -=35
		else:
			print("You step behind the wizard and swing with all your might hitting the wizard in the back. With a loud crunch his spine breaks and his lifeless corpse falls to the ground")
			print("A bright light shines down on you and the godess appears. She congratulates you and sends you to a village to live once more.")
			quit()#ends the game

#secret ending where player can throw coin found in first level at the wizard turning him into a frog
@when("flick gold coin at wizard")
@when("flick coin at wizard")
@when("throw gold coin at wizard")
@when("throw coin at wizard")
def frog_coin():
	global current_room
	global wizard_health
	if current_room == Wizard_lair and inventory.find("coin") and wizard_health >=1:
		print("You take the coin out of your pocket and throw it at the wizard. As it hits him, a cloud of green smoke appears . As the gas disperses, where the wizard once stood is now a frog.")
		print("A bright light shines down on you and the godess appears. She congratulates you and sends you to a village to live once more.")
		wizard_health -= 200
		quit()#ends the game




#If player health is less than or equal to 0, The game ends
if player_health <=0:
	print("You've sustained too much damage. You fall to the ground in agony, as your vision fades to black the last thing you see is your enemy towering above you.")
	quit()

#starts the game
def main():
	print("""
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		^^^^^^^^^^^^^^^^^^^^ \_*_\ Paladin's Plight /_*_/ ^^^^^^^^^^^^^^^^^^^^^
		^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		""")
	print("You are Desmond, the great hero of the west, and you are a paladin. After returning after defeating the dreadful beast in the Cave Of Sorrows, you hear of a wicked wizard in Alastair and decide to investigate. Upon your arrival,  you discover a red-clad wizard. He addresses you and tells you to leave. You respond by informing him that he is the one who must depart. With broadsword in hand, racing up to the wizard, as your blade slices through him, a plume of crimson smoke clouds your vision , leaving you unconscious.")
	print("Your body and the world slowly shrink as you fly up into the heavens. As you look up a sharp white light appears. As the light begins to fade a Goddess appears. 'You have accomplished great deeds, and have made the world a better place. Therefore' she continues 'I will give you another chance at life. But in order to live another life you must first defeat the wizard. I will send you to his labyrinth, where you can find him.' She says. 'Be careful though, I only have the power to send you body back. This means that you won't have your armor or your weapons. If you're lucky, You can find some scattered across his labyrinth. She smiles and you regain consciousness in a dim lit room.\n\n")
	start()

if __name__ == '__main__':
	main() 