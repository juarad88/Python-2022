from adventurelib import *
#All new code goes here

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

murials_tomb = Room(""" After walking through the door you walk down a passage way enscribed with ancient language. You are able to make out some of it but not all. "Long ago there was a soldier.... Blessed by the godesss.....said to have magic powers..... Soldier buried here." You continue walking to see the walkway open into a big dusty tomb.
	""")

#starts the game
def main():
	print("You are Desmond, the great hero of the west, and you are a paladin. After returning after defeating the dreadful beast in the Cave Of Sorrows, you hear of a wicked wizard in Alastair and decide to investigate. Upon your arrival,  you discover a red-clad wizard. He addresses you and tells you to leave. You respond by informing him that he is the one who must depart. With broadsword in hand, racing up to the wizard, as your blade slices through him, a plume of crimson smoke clouds your vision , leaving you unconscious.")
	print("Your body and the world slowly shrink as you fly up into the heavens. As you look up a sharp white light appears. As the light begins to fade a Goddess appears. 'You have accomplished great deeds, and have made the world a better place. Therefore' she continues 'I will give you another chance at life. But in order to live another life you must first defeat the wizard. I will send you to his labyrinth, where you can find him.' She says. 'Be careful though, I only have the power to send you body back. This means that you won't have your armor or your weapons. If you're lucky, You can find some scattered across his labyrinth. She smiles and you regain consciousness in a dim lit room.")
	start()

if __name__ == '__main__':
	main() 