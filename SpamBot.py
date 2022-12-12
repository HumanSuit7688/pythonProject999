import pyautogui
import pyperclip
import time


time.sleep(5)


def spam_bot(text: str, count: int):
    pyperclip.copy(text)
    for i in range(count):
        time.sleep(0.01)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")


spam_bot("Попов - сын бляди!", 50)
