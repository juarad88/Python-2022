from adventurelib import *
#All new code goes here

#rooms
space = Room("""
	You are drifiting in space. It feels very cold.
	A slate-blue spaceship sits completely silently to your left, its airlock open and waiting
	""")

airlock = Room("""
	The airlock of the spaceship is a pristine white, with a small, red, button which opens and closes the lock.
	""")
cargo = Room("""You enter the cargo room. It's filled with massive crates that all have a foreign language written on the side and top. Some seem to be locked others not.
	""")
docking = Room(""" You enter a vast open room filled with smaller spaceships""")

hallway = Room("""You enter the hallway. It's a well lit corridor with a many doors on each side.""")

bridge = Room("""The bridge of the spaceship is shiny and white, with thousands of small, red, blinking lights""")

quarters = Room("""You enter a room that provides a view of the enourmous and colourful solar sytem outside. YOu walk down a few stairs to see long scortch marks on the glass and floor. Shattered contorl pannels with a few mangles corpses on the floor. Yellow blood splattered everywhere.""")

mess_hall = Room("""You enter a room that appears to resemlbe a mess hall. There are tables flipped upside down with the same black scorch marks as in the quarters. Once again there are corpses lying on the floor. """)

escape_pods = Room("""You reach the final destination on the spaceship. It's a white room with circular doors on each side. 'Escape pods' you think. You go to unlock one but find that it's already gone. You check the others but find the same result. You are going to need to find an alternate exit out of the spaceship""")
#exits
airlock.east = hallway
airlock.south = quarters
hallway.east = bridge
hallway.north = cargo
quarters.east = mess_hall
mess_hall.north = hallway
mess_hall.east = escape_pods
escape_pods.north = bridge

#items
item.description = ""#description of item goes inside speech marks

knife = Item("a dirty knife", "knife")
knife.description = "The knife has a dull sheen to it but it looks rather sharp"

red_keycard = Item("a red keycard","keycard","red card", "card")
red_keycard.description = "It's as red keycard. It probably opens a door or locker"

blaster = Item("blaster","gun","rilfe", "handgun")
blaster.description = "The blaster is small enought to carry. It looks futuristic and shoots red lasers."

#variables
current_room = space
print(current_room)
#binds
@when ("DIRECTION")
@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)
@when("look around")
@when("look")
def look():
	global current_room
	print(current_room)
	print(current_room.exits())

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room
#check if action can be done
	if current_room is not space:
		say("There is no airlock here")
		return
	else:
		current_room = airlock
		print("""You heave yourself into the spaceship and 
			slam your hand on the button to close the door.
			""")
		print(current_room)



#starts the game
def main():
	start()

if __name__ == '__main__':
	main()