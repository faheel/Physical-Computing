from gpiozero import DigitalOutputDevice


# Display segments
a = DigitalOutputDevice(6)
b = DigitalOutputDevice(12)
c = DigitalOutputDevice(13)
d = DigitalOutputDevice(19)
e = DigitalOutputDevice(16)
f = DigitalOutputDevice(26)
g = DigitalOutputDevice(20)

# Segments to turn on for the given input
segments = {
	'0': [a, b, c, d, e, f],
	'1': [b, c],
	'2': [a, b, g, e, d],
	'3': [a, b, g, c, d],
	'4': [f, g, b, c],
	'5': [a, f, g, c, d],
	'6': [a, f, e, d, c, g],
	'7': [a, b, c],
	'8': [a, b, c, d, e, f, g],
	'9': [a, f, g, b, c],
	'A': [a, f, e, b, c, g],
	'B': [f, e, g, c, d],
	'C': [a, f, e, d],
	'D': [b, c, g, e, d],
	'E': [f, e, a, g, d],
	'F': [f, e, a, g],
}


def display(character):
	for segment in segments['8']:	# turn all segments off
		segment.off()

	for segment in segments[character.upper()]:		# turn on the required segments
		segment.on()


while True:
	character = input()
	display(character)

