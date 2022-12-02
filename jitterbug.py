

import pyautogui
import time
from random import random
import winsound
import keyboard
from threading import Thread

def exit():
    global done
    print('Exiting...')
    done = True

# exit the program if esc is pressed
keyboard.add_hotkey('esc', exit)

def next_letter():
    while True:
        for letter in 'jitterbug ':
            yield letter

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def open_notepad_and_type_jitterbug():
    global done
    # open notepad and type jitterbug
    pyautogui.hotkey('win', 'r')
    time.sleep(0.1)
    pyautogui.typewrite('notepad')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
    while True:
        for letter in next_letter():
            if done:
                return
            time.sleep(0.1)
            pyautogui.press(letter)

pyautogui.FAILSAFE = True

duration = 0.1
distance = 1
iterations = 0
verbose = False

def play_jitterbug_loop():
    global done
    # play jitterbug_loop.wav on a loop with playsound module
    while not done:
        winsound.PlaySound('notification.wav', winsound.SND_FILENAME)


done = False
def jitterbug():
    global done
    # wait ten seconds, then wait until the user moves the mouse
    time.sleep(10)
    starting_position = pyautogui.position()
    while pyautogui.position() == starting_position:
        time.sleep(0.1)
    if verbose:
        print("Detected mouse movement")
    # bump around the mouse cursor a little bit with pyautogui
    iterations = 0
    slow_down = 1
    while not done:
        time.sleep((random() * 10) / (iterations + 1) * slow_down)
        if verbose:
            print('jitterbug', iterations)
        x_distance = int((random() - 0.5) * iterations)
        y_distance = int((random() - 0.5) * iterations)
        pyautogui.moveRel(x_distance, y_distance, duration=duration)
        iterations += 1
        song_start = 40
        # if iterations goes to song_start, start playing the jitterbug loop
        if iterations == song_start:
            Thread(target=play_jitterbug_loop).start()
notepad = False
if __name__ == '__main__':
    if notepad:
        Thread(target=open_notepad_and_type_jitterbug).start()
    jitterbug()
