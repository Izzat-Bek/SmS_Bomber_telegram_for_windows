import pyautogui
import random
import time
import os
from art import tprint


def sms_bomber_telegram_in_windows(n: int, lis: list, who: str):
    pyautogui.press('win')
    pyautogui.write('telegram')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(who)
    time.sleep(2)
    pyautogui.press('enter')

    for i in range(n):
        if len(lis) > 1:
            pyautogui.write(lis[random.randint(0, len(lis) - 1)])
            pyautogui.press('enter')
        else:
            pyautogui.write(lis[0])
            pyautogui.press('enter')
    time.sleep(1)
    pyautogui.keyDown('alt')
    time.sleep(0.5)
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
    return "Bajarildi"


def main():
    os.system("cls")
    os.system("color 4")
    time.sleep(0.2)
    tprint('SMS BOMBER IN TELEGRAM', font='cybermedum')
    n = int(input("Necta sms jonatiwni korsating: \n"))
    s = int(input("smslar toplamini sonini kiriting: \n"))
    lis = []
    for i in range(s):
        h = input("sms kiriting: \n")
        lis.append(h)

    who = input("\nsms ni kimga jonatish kere: \nnikini kiriting: \n")
    exam = sms_bomber_telegram_in_windows(n, lis, who)
    print(exam)
    s = input("Enter to exit")


if __name__ == '__main__':
    main()
