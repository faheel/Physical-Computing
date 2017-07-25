from gpiozero import PWMLED
from signal import pause


led = PWMLED(17)	# LED with variable brightness, on GPIO pin 17
led.pulse()

pause()		# keep the script running

