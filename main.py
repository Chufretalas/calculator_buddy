import subprocess
import pyautogui as pgui

# https://github.com/asweigart/PyGetWindow/issues/36
from pygetwindow import getWindowsWithTitle

from time import sleep


def main():
    calcProcess = subprocess.Popen(r"C:\Windows\System32\calc.exe")

    sleep(1)

    calc_window = getWindowsWithTitle("Calculadora")[0]
    if not calc_window.isActive:
        pgui.press("altleft")
        calc_window.activate()

    buttonx, buttony = pgui.locateCenterOnScreen("./buttons/8.png")
    pgui.click(buttonx, buttony)


if __name__ == "__main__":
    main()
