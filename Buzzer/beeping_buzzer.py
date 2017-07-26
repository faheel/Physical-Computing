from gpiozero import Buzzer
from signal import pause


buzzer = Buzzer(17)	# piezoelectric buzzer on GPIO pin 17
buzzer.beep()

pause()

