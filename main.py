import subprocess
import os
from time import sleep
import pyautogui as pgui

# https://github.com/asweigart/PyGetWindow/issues/36
from pygetwindow import getWindowsWithTitle


def test_all():
    for img in os.listdir("./buttons"):
        try:
            buttonx, buttony = pgui.locateCenterOnScreen(
                f"./buttons/{img}", confidence=0.9
            )
            pgui.click(buttonx, buttony)
        except pgui.ImageNotFoundException as e:
            print(f"Did not find {img}")
            print(e)


def click_button(file_name: str):
    try:
        buttonx, buttony = pgui.locateCenterOnScreen(
            f"./buttons/{file_name}", confidence=0.9
        )
        pgui.click(buttonx, buttony)
    except pgui.ImageNotFoundException as e:
        print(f"Did not find {file_name}")
        print(e)


def main():
    calcProcess = subprocess.Popen(r"C:\Windows\System32\calc.exe")

    sleep(0.2)

    while True:

        commands: str = pgui.prompt(
            "Please type desired sequence of commands. Use * and /  for multiplication and division."
        )

        sleep(0.1)

        calc_window = getWindowsWithTitle("Calculadora")[0]
        if not calc_window.isActive:
            pgui.press("altleft")
            calc_window.activate()

        sleep(0.1)

        for c in commands:
            if c.isnumeric():
                click_button(f"{c}.png")
                continue

            match c.lower():
                case "c":
                    click_button("c.png")

                case ",":
                    click_button("comma.png")

                case ".":
                    click_button("comma.png")

                case "/":
                    click_button("div.png")

                case "=":
                    click_button("equals.png")

                case "-":
                    click_button("minus.png")

                case "*":
                    click_button("mul.png")

                case "+":
                    click_button("plus.png")


if __name__ == "__main__":
    main()
