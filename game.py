from adventurelib import *
#All new code goes here

starting_room = Room(""" You look around and see a small wooden desk in one corner of the room, a bookshelf in another and a cupboard against one of the walls. In front of you is a door with some kind of lock on it.
	""")

store_room = Room(""" As you enter the room you see large old dusty crates stacked upon each other. You see a old wooden door with no lock on to your right
	""")

weapon_room = Room(""" You stroll inside the next room. Inside you see racks and racks filled with a large assortment of weapons. Swords, axes, spears and hammers. Once again there is a dorr wit a lock on it.
	""") 

twisted_caverns = Room(""" The door opens to a vast room with 3 tinnels, and a goblin warrior guarding them. He appears to be holding some type of rusty dagger
	""")




#starts the game
def main():
	print("You are Desmond, the great hero of the west, and you are a paladin. After returning after defeating the dreadful beast in the Cave Of Sorrows, you hear of a wicked wizard in Alastair and decide to investigate. Upon your arrival,  you discover a red-clad wizard. He addresses you and tells you to leave. You respond by informing him that he is the one who must depart. With broadsword in hand, racing up to the wizard, as your blade slices through him, a plume of crimson smoke clouds your vision , leaving you unconscious.")
	print("Your body and the world slowly shrink as you fly up into the heavens. As you look up a sharp white light appears. As the light begins to fade a Goddess appears. 'You have accomplished great deeds, and have made the world a better place. Therefore' she continues 'I will give you another chance at life. But in order to live another life you must first defeat the wizard. I will send you to his labyrinth, where you can find him.' She says. 'Be careful though, I only have the power to send you body back. This means that you won't have your armor or your weapons. If you're lucky, You can find some scattered across his labyrinth. She smiles and you regain consciousness in a dim lit room.")
	start()

if __name__ == '__main__':
	main() 