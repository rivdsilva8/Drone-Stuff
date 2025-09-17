from djitellopy import Tello
from time import sleep

tello = Tello()

tello.connect()
tello.takeoff()
print(tello.get_battery())

tello.rotate_clockwise(90)
sleep(2)
tello.rotate_counter_clockwise(90)
sleep(2)
tello.land()
