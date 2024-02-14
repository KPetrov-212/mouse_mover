import pyautogui
import random
import time
import tkinter as tk
from tkinter import Button
from threading import Thread

class AutoGUIController:
    def __init__(self, root):
        self.root = root
        self.running = False

        self.start_button = Button(root, text="Start", command=self.start_program)
        self.start_button.pack(pady=50, padx=150)

        self.stop_button = Button(root, text="Stop", command=self.stop_program, state=tk.DISABLED)
        self.stop_button.pack(pady=50, padx=150)

    def start_program(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.running = True
        Thread(target=self.run_program).start()

    def stop_program(self):
        self.running = False

    def check_stop(self):
        if not self.running:
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
        else:
            self.root.after(100, self.check_stop)

    def move_mouse(self):
        pyautogui.moveTo(5, pyautogui.size()[1], duration=1)

    def click_mouse(self):
        pyautogui.click()

    def run_program(self):
        while self.running:
            self.move_mouse()
            self.click_mouse()
            time.sleep(5)

        self.check_stop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("AutoGUI Controller")

    auto_gui_controller = AutoGUIController(root)

    root.after(100, auto_gui_controller.check_stop)
    root.mainloop()
