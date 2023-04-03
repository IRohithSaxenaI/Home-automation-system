import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)


def main():
    motion = False
    door = False


while True:
    if GPIO.input(13):
        if motion == False:
            print('Motion Detected')
            motion = True
else:
    motion = False
if GPIO.input(15):
    if door == False:
        print('Door Opened')
    door = True
else:
    door = False
    time.sleep(.3)
if __name__ == ('__main__'):
    main()
