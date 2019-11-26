import RPi.GPIO as GPIO


class Led:

    def __init__(self, pin, mode):
        self.pin = pin
        self.mode = mode

    def turn_on(self):
        pass

    def turn_off(self):
        pass


class IndoorLed(Led):

    def __init__(self, pin, mode):
        Led.__init__(self, pin, mode)

    def turn_on(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
