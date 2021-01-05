##from pynput.keyboard import Controller, Listener
import keyboard
from time import sleep
from random import randint

def randslp():
    sleep(randint(10, 30)/1000)
    if randint(1, 100) == 2:
        sleep(0.1)
    if randint(1, 1000) == 2:
        sleep(1)

def longpress(c, t = 0.420): 
    keyboard.press(c)
    sleep(t)
##    randslp()
    keyboard.release(c)
    randslp()

start = ','
end = '.'
                                            
print('Press', start)
keyboard.wait(start)

    
while True:
    longpress('a')
##    keyboard.press_and_release('1')
    longpress('d')
    keyboard.press_and_release('1')
    
    if keyboard.is_pressed(end):
        print('Awaiting resume order')
        print('Press', start)
        keyboard.wait(start)
        print('Resumed \n')
        print(f'Press {end} to stop')
