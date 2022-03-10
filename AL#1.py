from adventurelib import *
#All new code goes here
@when("brush teeth")
@when("brush")
@when("clean teeth")
def brush_teeth():
	print("You brush your teeth")
@when("comb hair")
@when("comb")
def comb_hair():
	say("""
		You brush your long flowing locks with the gold hairbrush that you have selected form the red basket.
		""")


#starts the game
def main():
	start()

if __name__ == '__main__':
	main()
