from adventurelib import *
Room.items = Bag()
inventory = Bag()
#All new code goes here

#rooms
starting_room = Room(""" You look around and see a small wooden desk in one corner of the room, a bookshelf in another and a cupboard against one of the walls. In front of you is a door with some kind of lock on it.
	""")

store_room = Room(""" As you enter the room you see large old dusty crates stacked upon each other. You see a old wooden door with no lock on to your right
	""")

weapon_room = Room(""" You stroll inside the next room. Inside you see racks and racks filled with a large assortment of weapons. Swords, axes, spears and hammers. Once again there is a dorr wit a lock on it.
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



#Define bags
starting_room.items.add(gold_coin)


current_room = starting_room

#binds
@when("look")
@when("look around")
def look():
	global current_room
	print(current_room)


@when("go to desk")
@when("go to wooden desk")
@when("search desk")
@when("search wooden desk")
def search_desk():
	print("You walk up to the desk investigating it. The desk is rather small and made of smooth oak. On the desk sits a candle. The candle is the only light source in the room. The desk has a drawer that can be opened")

@when("open drawer")
@when("search drawer")
@when("look in drawer")
def seacrh_drawer():
	print("You open the drawer. Inside are some blank pieces of paper as well as a single gold coin")

@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a {item}")

@when("inventory")
@when("show inventory")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

@when("look at bookshelf")
@when("search bookshelf")
@when("go to bookshelf")
def search_bookshelf():
	print("You walk over to the dusty bookshelf. On the racks are many books, some different sizes and colours")

@when("take book")
def take_book():
	print("As you go to take a book of the shelf, you find that the book won't move. On frustration you pull the book and and low grumbling sound. After a few seconds the entire bookshelf has moved to one side, revealing a sectret room")

@when("enter")
@when("enter secret room")
def secret_room():
	print(""""You enter the scret room\n
		Inside is a wooden table filled with papers with some strange writting that you cannot read""")

#starts the game
def main():
	print("You are Desmond, the great hero of the west, and you are a paladin. After returning after defeating the dreadful beast in the Cave Of Sorrows, you hear of a wicked wizard in Alastair and decide to investigate. Upon your arrival,  you discover a red-clad wizard. He addresses you and tells you to leave. You respond by informing him that he is the one who must depart. With broadsword in hand, racing up to the wizard, as your blade slices through him, a plume of crimson smoke clouds your vision , leaving you unconscious.")
	print("Your body and the world slowly shrink as you fly up into the heavens. As you look up a sharp white light appears. As the light begins to fade a Goddess appears. 'You have accomplished great deeds, and have made the world a better place. Therefore' she continues 'I will give you another chance at life. But in order to live another life you must first defeat the wizard. I will send you to his labyrinth, where you can find him.' She says. 'Be careful though, I only have the power to send you body back. This means that you won't have your armor or your weapons. If you're lucky, You can find some scattered across his labyrinth. She smiles and you regain consciousness in a dim lit room.\n\n")
	start()

if __name__ == '__main__':
	main() 