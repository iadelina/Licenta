import RPi.GPIO as GPIO
GPIO.cleanup()
from abc import abstractmethod, ABCMeta

class Led:
    _metaclass_ = ABCMeta
    def __init__(self, pin, mode):
        self.pin = pin
        self.mode = mode
        GPIO.cleanup()

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class IndoorLed(Led):

    def __init__(self, pin, mode):
        Led.__init__(self, pin, mode)

    def turn_on(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def get_current_state(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN)
        state = GPIO.input(self.pin)
        GPIO.cleanup()
        return 'APRINS' if state else 'STINS'
