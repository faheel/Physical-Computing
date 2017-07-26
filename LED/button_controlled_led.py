from gpiozero import LED, Button
from time import sleep


led = LED(17)	# LED on GPIO pin 17
button = Button(2)	# push button on GPIO pin 2

while True:
	button.wait_for_press()
	led.toggle()
	
	if led.is_lit:
		print('LED is switched on')
	else:
		print('LED is switched off')
	
	sleep(0.1)	# to ignore extra input while pushing and releasing the button

