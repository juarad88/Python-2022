from adventurelib import *
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

twisted_caverns = Room(""" The door opens to a vast room with 3 tunnels, and a goblin warrior guarding them. He appears to be holding some type of rusty dagger.
	""")

cavern_1 = Room(""" You venture down the 1st cavern. \n After walking in complete darkness for a few minutes a green glowing light appears around a bend in the tunnel. Upon arrival you see a small bugs flying in the air all emitting a faint green glow. In the fain tlight you see a corpse wearing gold plated armour.
	""")

cavern_2 = Room(""" You venture down the 2nd cavern. \n After walking in complete darkness for a few minutes a green glowing light appears around a bend in the tunnel. Upon arrival you see a small bugs flying in the air all emitting a faint green glow. In the fain tlight you see a corpse cluting a sack.
	""")

cavern_3 = Room(""" You venture down the 3rd cavern. \n After walking in complete darkness for a few minutes a green glowing light appears around a bend in the tunnel. Upon arrival you see a small bugs flying in the air all emitting a faint green glow. In the fain tlight you see a corpse with a war javelin stuck inside it.
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

Wizard_lair = Room("""The door opens into a vast stone room. Stairs start to climb up reaching a huge throne high above the ground. On each side of the thorne flames flicker, lighting up the room. Sitting comfortabely on the throne is The wizard that killed you.. he stands up then dissapears, reemerging in front of you. "Back again are we?" He asks. You tighten your grip on your weapon.
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

morningstar = Item("mace")
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
	if item in inventory:
		f=inventory.find(item)
		print(f.description)
	elif item == "clothes":
		print("You take a closer look at the clothes but find they are too small to wear")
	elif item == "book":
		print("As you go to take a book off the shelf, you find that the book won't move. In frustration you pull the book and and low grumbling sound. After a few seconds the entire bookshelf has moved to one side, revealing a secret room")
		@when("enter")
		@when("enter secret room")
		def secret_room():
			print("""You enter the secret room. Inside is a wooden table filled with papers with some strange writting that you cannot read Holding them together is a paper clip""")
	elif item == "sword" and axe not in inventory and spear not in inventory and morningstar not in inventory:
		print(f"You pick up the {item}")
		print(Item.description())
	elif item == "axe" and sword not in inventory and spear not in inventory and morningstar not in inventory:
		print(f"You pick up the {item}")
		print(Item.description())
	elif item == "spear" and axe not in inventory and sword not in inventory and morningstar not in inventory:
		print(f"You pick up the {item}")
		print(Item.description())
	elif item == "morningstar" and axe not in inventory and spear not in inventory and sword not in inventory:
		print(f"You pick up the {item}")
		print(Item.description())
	else:
		print(f"You can't take {item}")








@when("inventory")
@when("show inventory")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

#1st room
@when("look at bookshelf")
@when("search bookshelf")
@when("go to bookshelf")
@when("look at book shelf")
@when("search book shelf")
@when("go to book shelf")
def search_bookshelf():
	print("You walk over to the dusty bookshelf. On the racks are many books, some different sizes and colours")

@when("go to cupboard")
@when("search cupboard")
@when("look at cupboard")
def search_cupboard():
	print("You go over to the cupboard . It is tall and made of a dark oak. You open it revealing some old clothes.")


@when("go to desk")
@when("go to wooden desk")
@when("search desk")
@when("search wooden desk")
def search_desk():
	print("You walk up to the desk investigating it. The desk is rather small and made of smooth oak. On the desk sits a candle. The candle is the only light source in the room. The desk has a drawer that can be opened")

@when("open drawer")
@when("search drawer")
@when("look in drawer")
@when("open draw")
@when("search draw")
@when("look in draw")
def seacrh_drawer():
	print("You open the drawer. Inside are some blank pieces of paper as well as a single gold coin")

@when("use paper clip")
@when("use paperclip")
#@when("go to door")
#@when("go to lock")
#@when("pick lock")
def pick_lock():
	if inventory.find("paper clip") and current_room == starting_room:
		print("You go to the door and unfold the paper clip and insert it into the lock. After turning it around a few times you hear a soft click, and the lock is off.")	
		global door_opened
		door_opened = True
	else:
		print("You don't have the equipment to pick the lock")
		
		                         
                       
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
	else:
		print("The door is locked")




#2nd Room
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

@when("eat jerky")
@when("use jerky")
@when("eat  beef jerky")
@when("eat dried beef jerky")
@when("use beef jerky")
@when("use dried beef jerky")
def eat_jerky():
	if inventory.find("beef jerky"):
		global player_health
		if player_health > 100:
			player_health += 20
			print("You eat the jerky. It's tough but doesn't taste too bad") 
		elif player_health < 100:
			player_health = 100
			print("You eat the jerky. It's tough but doesn't taste too bad")
		elif player_health == 100:
			print("Health is full")
			player_health = 100
		inventory.take("jerky")

@when("player health")
@when("health")
@when("show player health")
@when("show health")
def show_health():
	print(player_health)


#3rd room
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
	print("You inspect the wepon racks. There are plenty of weapons to chose from. You are only strong enough to carry one weapon. What weapon will you chose? Axe, sword, spear or morningstar")



	

	








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