

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
        for letter in 'get rekt m8 lol xd 420 blaze it 69 ':
            yield letter

alphabet = 'abcdefghijklmnopqrstuvwxyz'
time_to_wait = 5
letter_generator = next_letter()
def backspace_then_type():
    while True:
        for letter in alphabet:
            if keyboard.is_pressed(letter):
                pyautogui.press('backspace')
                current_letter = next(letter_generator)
                print("\n\ncurrent letter:", current_letter)
                pyautogui.keyDown(current_letter)
                pyautogui.keyUp(current_letter)
                time.sleep(0.1)
                break
        time.sleep(0.1)

pyautogui.FAILSAFE = True

duration = 0.1
distance = 1
iterations = 0

def play_jitterbug_loop():
    # play jitterbug_loop.wav
    winsound.PlaySound('jitterbug.wav', winsound.SND_FILENAME)

done = False
def jitterbug():
    global done
    # wait until the user moves their mouse
    starting_position = pyautogui.position()
    while pyautogui.position() == starting_position:
        time.sleep(0.1)
    # bump around the mouse cursor a little bit with pyautogui
    iterations = 0
    while not done:
        time.sleep(random() / (iterations + 1) * 0.1)
        print("jitterbug")
        x_distance = int((random() - 0.5) * iterations)
        y_distance = int((random() - 0.5) * iterations)
        pyautogui.moveRel(x_distance, y_distance, duration=duration)
        iterations += 1
        # if iterations goes to 100, start playing jitterbug.wav
        if iterations == 100:
            winsound.PlaySound('jitterbug.wav', winsound.SND_FILENAME)

if __name__ == '__main__':
    typing_thread = Thread(target=backspace_then_type)
    typing_thread.start()
    play_jitterbug_loop()
    jitterbug()