from adventurelib import *
#All new code goes here
space = Room("""
	You are drifiting in space. It feels very cold.
	A slate-blue spaceship sits completely silently to your left, its airlock open and waiting
	""")

spaceship = Room("""
	The bridge of the spaceship is shiny and white, with thousands of small, red, blinking lights
	""")

current_room = space

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
		current_room = spaceship
		print("""You heave yourself into the spaceship and 
			slam your hand on the button to close the door.
			""")
		print(current_room)



#starts the game
def main():
	start()

if __name__ == '__main__':
	main()