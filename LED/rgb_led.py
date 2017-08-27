from gpiozero import RGBLED
from time import sleep


led = RGBLED(red=17, green=27, blue=22)
LED_IS_COMMON_ANODE_TYPE = True		# set this to False if LED is common-cathode type

colours = {	  # (r, g, b)
	"black":	(0, 0, 0),
	"red":		(1, 0, 0),
	"green":	(0, 1, 0),
	"blue":		(0, 0, 1),
	"yellow":	(1, 1, 0),
	"magenta":	(1, 0, 1),
	"cyan":		(0, 1, 1),
	"white":	(1, 1, 1)
}

def print_available_colours():
	for key in colours.keys():
		print(key, end=", ")
	print("\b\b ")      # erase the trailing comma


# invert on/off values if LED is common-anode type
if LED_IS_COMMON_ANODE_TYPE:
	for key in colours.keys():
		colours[key] = tuple(abs(value - 1) for value in colours[key])

print("Press Ctrl+C to exit\n")

print("Available colours:")
print_available_colours()

while True:
	try:
		colour = input("\nEnter a colour: ")
		try:
			led.color = colours[colour]
			print("LED colour changed to {}".format(colour))
		except KeyError:
			print("That's no colour! Try one of these:")
			print_available_colours()
	except KeyboardInterrupt:
		print()
		break

