from gpiozero import LED, Button
from signal import pause

led = LED(17)	# LED on GPIO pin 17
button = Button(2)	# push button on GPIO pin 2

led.source = button.values

pause()

