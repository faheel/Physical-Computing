from gpiozero import Button, Buzzer, LED
from signal import pause


button = Button(2)	# push button on GPIO pin 2
buzzer = Buzzer(27)	# buzzer on GPIO pin 27
led = LED(17)		# LED on GPIO pin 17

buzzer.source = led.source = button.values

pause()

