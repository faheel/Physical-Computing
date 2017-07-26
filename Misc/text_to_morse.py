from gpiozero import Buzzer, LED
from time import sleep


buzzer = Buzzer(27)	# buzzer on GPIO pin 27
led = LED(17)		# LED on GPIO pin 17

led.source = buzzer.values

dot_duration = 0.05	# seconds
morse = {
	' ': ' ',
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.', 
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'
}

while True:
	line = input("Text: ")
	for word in line:
		for letter in word:
			print(letter, end='', flush=True)
			for symbol in morse[letter.upper()]:
				print(symbol, end='', flush=True)
				if symbol == '.':
					buzzer.beep(dot_duration, n=1, background=False)
				elif symbol == '-':
					buzzer.beep(dot_duration * 3, n=1, background=False)
				sleep(dot_duration)
			print(' ', end='', flush=True)
			sleep(dot_duration * 2)	# 3-1 = 2
		sleep(dot_duration * 4)	# 7-3 = 4
	print()

