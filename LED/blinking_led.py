from gpiozero import LED
from signal import pause


led = LED(17)	# LED on GPIO pin 17
led.blink()

pause()		# keep the script running

